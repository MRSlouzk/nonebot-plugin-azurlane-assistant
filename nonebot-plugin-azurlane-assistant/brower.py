# Python Script Created by MRS
from typing import Tuple
from io import BytesIO

from nonebot.log import logger
from playwright.async_api import Browser, async_playwright, Playwright, Page, Error
from PIL import Image

async def start() -> Tuple[Browser, Playwright]:
    _playwright = await async_playwright().start()
    try:
        _brower = await _playwright.chromium.launch(headless=True)
    except Error:
        await install()
        _brower = await _playwright.chromium.launch(headless=True)
    return (_brower, _playwright)

async def get_brow(_brower: Browser) -> Browser:
    return _brower if _brower and _brower.is_connected() else await start()

async def shut(_brower: Browser, _playwright: Playwright):
    assert _brower and _playwright
    await _brower.close()
    _playwright.stop()

# 本部分代码参考https://github.com/kexue-z/nonebot-plugin-htmlrender/blob/master/nonebot_plugin_htmlrender/browser.py进行编写
async def install():
    import os
    import sys

    from playwright.__main__ import main

    logger.info("使用镜像源进行下载")
    os.environ[
        "PLAYWRIGHT_DOWNLOAD_HOST"
    ] = "https://npmmirror.com/mirrors/playwright/"
    success = False

    logger.info("正在安装 chromium")
    sys.argv = ["", "install", "chromium"]
    try:
        logger.info("正在安装依赖")
        os.system("playwright install-deps")
        main()
    except SystemExit as e:
        if e.code == 0:
            success = True
    if not success:
        logger.error("浏览器更新失败, 请检查网络连通性")

async def open_ship_fleet_simulator(_brower: Browser, code: str, *args, simulator_type: str = "bwiki") -> bytes:
    if(not _brower): raise Exception("未安装playwright,无法使用本功能")
    if(simulator_type == "bwiki"):
        url = "https://wiki.biligame.com/blhx/%E8%88%B0%E9%98%9F%E6%A8%A1%E6%8B%9F%E5%99%A8"
    elif(simulator_type == "x94fujo6rpg"):
        raise Exception("因为技术性问题,暂不支持x94fujo6rpg制作的AzureLaneFleet舰队模拟器解析,请见谅")
    else:
        url = "https://wiki.biligame.com/blhx/%E8%88%B0%E9%98%9F%E6%A8%A1%E6%8B%9F%E5%99%A8"
    page = await _brower.new_page(java_script_enabled=True, viewport={"width": 1920, "height": 1080}, is_mobile=False)
    await page.goto(url)
    await page.fill("//textarea[@id=\"fleetdata\"]", code)
    await page.click("//button[@id=\"loadDataByID\"]")
    await page.wait_for_function("loadDataByID")
    res = await page.query_selector("//*[@id=\"AzurLaneFleetApp\"]/div/div[2]")
    await res.scroll_into_view_if_needed()
    box = await res.bounding_box()
    img = await page.screenshot(type="png", clip=box)
    return img