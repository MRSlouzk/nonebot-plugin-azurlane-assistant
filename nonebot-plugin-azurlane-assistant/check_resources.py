# Python Script Created by MRS
from nonebot import get_driver
from nonebot.log import logger

import asyncio, pathlib, os, json
import hashlib

from .utils import get_content
from .config import config

DATA_PATH = "./src/data/azurlane/"

async def update_res():
    def get_json() -> dict:
        jinghao: dict = await get_content(
            "https://github.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/raw/main/data/jinghao_rank.json")
        build_pool: dict = await get_content(
            "https://github.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/raw/main/data/pool.json")
        with open(DATA_PATH + "data/jinghao_rank.json", "w", encoding="utf-8") as f:
            json.dump(jinghao, f)
        with open(DATA_PATH + "data/pool.json", "w", encoding="utf-8") as f:
            json.dump(build_pool, f)
        return jinghao

    if(not os.path.exists(DATA_PATH)):
        logger.warning("资源文件夹不存在，正在创建...")
        os.makedirs(DATA_PATH)
        os.makedirs(DATA_PATH + "data")
        os.makedirs(DATA_PATH + "img/jinghao_rank")

        jh = get_json()

        for items in jh.values():
            name = items["name"]
            url = "https://github.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/blob/main/img/jinghao_rank/" + name
            img = await get_content(url, proxies=config.az_proxy)
            with open(DATA_PATH + "img/jinghao_rank/" + name, "wb") as f:
                f.write(img)
    else:
        jh = get_json()
        for items in jh.values():
            name = items["name"]
            raw_hash = items["hash"]
            if hashlib.md5(open(DATA_PATH + "img/jinghao_rank/" + name, "rb").read()).hexdigest() == raw_hash:
                continue
            else:
                url = "https://github.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/blob/main/img/jinghao_rank/" + name
                img = await get_content(url, proxies=config.az_proxy)
                with open(DATA_PATH + "img/jinghao_rank/" + name, "wb") as f:
                    f.write(img)

driver = get_driver()
@driver.on_startup
def _():
    logger.info("正在更新资源文件...")
    asyncio.ensure_future(update_res())