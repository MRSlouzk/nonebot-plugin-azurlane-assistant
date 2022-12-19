# Python Script Created by MRS
from typing import Tuple

from nonebot.log import logger
from playwright.async_api import Browser, async_playwright, Playwright, Page, Error

# 本部分代码参考https://github.com/kexue-z/nonebot-plugin-htmlrender/blob/master/nonebot_plugin_htmlrender/browser.py进行编写
async def start() -> Tuple[Browser, Playwright]:
    _playwright = await async_playwright().start()
    try:
        _brower = await _playwright.chromium.launch(headless=True)
    except Error:
        await install()
        _brower = await _playwright.chromium.launch(headless=True)
    return (_brower, _playwright)

async def shut(_brower: Browser, _playwright: Playwright):
    assert _brower and _playwright
    await _brower.close()
    await _playwright.stop()

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

async def open_ship_fleet_simulator(
        _brower: Browser,
        code: str,
        *args,
        simulator_type: str = "bwiki"
    ) -> bytes:
    """
    截图舰队模拟器

    :param _brower: 浏览器
    :param code: 舰队编码
    :param simulator_type: 模拟器类型
    :return: 截图
    :exception: 舰队编码不合法|舰队数据加载失败|暂不支持AzureLaneFleet
    """
    if(not code.isalnum()): raise Exception("舰队编码不合法")
    if(not _brower): raise Exception("未安装playwright或者playwright未正常启动,无法使用本功能")
    if(simulator_type == "bwiki"):
        url = "https://wiki.biligame.com/blhx/%E8%88%B0%E9%98%9F%E6%A8%A1%E6%8B%9F%E5%99%A8"
    elif(simulator_type == "x94fujo6rpg"):
        raise Exception("因为技术性问题,暂不支持x94fujo6rpg制作的AzureLaneFleet舰队模拟器解析,请见谅")
    else:
        url = "https://wiki.biligame.com/blhx/%E8%88%B0%E9%98%9F%E6%A8%A1%E6%8B%9F%E5%99%A8"
    page = await _brower.new_page(java_script_enabled=True, viewport={"width": 1920, "height": 1080}, is_mobile=False, locale="zh-CN")
    await page.goto(url)
    await page.fill("//textarea[@id=\"fleetdata\"]", code)

    async with page.expect_console_message() as console_info:
        await page.click("//button[@id=\"loadDataByID\"]")
    msg = await console_info.value
    if("save key" not in msg.text):
        await page.close()
        raise Exception("舰队数据加载失败, 请检查编码正确性")

    await page.wait_for_load_state("domcontentloaded")
    res = await page.query_selector("//*[@id=\"AzurLaneFleetApp\"]/div") #//*[@id=\"AzurLaneFleetApp\"]/div/div[2]
    await res.scroll_into_view_if_needed()
    box = await res.bounding_box()
    img = await page.screenshot(type="png", clip=box)
    await page.close()
    return img