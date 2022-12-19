# Python Script Created by MRS
from nonebot.log import logger

import os, json
import hashlib

from .modules.utils import get_content

DATA_PATH = "./data/azurlane/"

async def update_res():
    async def get_json():
        jinghao: str = await get_content("https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/data/jinghao_rank.json")
        build_pool: str = await get_content("https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/data/pool.json")
        japan_ship: str = await get_content("https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/data/japan_ship_name.json")
        (jinghao, build_pool, japan_ship) = json.loads(jinghao), json.loads(build_pool), json.loads(japan_ship)
        jinghao: dict
        with open(DATA_PATH + "data/jinghao_rank.json", "w", encoding="utf-8") as f0:
            json.dump((jinghao), f0, ensure_ascii=False, indent=4)
        with open(DATA_PATH + "data/pool.json", "w", encoding="utf-8") as f1:
            json.dump(build_pool, f1, ensure_ascii=False, indent=4)
        with open(DATA_PATH + "data/japan_ship_name.json", "w", encoding="utf-8") as f2:
            json.dump(japan_ship, f2, ensure_ascii=False, indent=4)
        return jinghao

    if(not os.path.exists(DATA_PATH)):
        logger.warning("资源文件夹不存在，正在创建...")
        os.makedirs(DATA_PATH)
        os.makedirs(DATA_PATH + "data/")
        os.makedirs(DATA_PATH + "img/jinghao_rank")

        logger.info("开始下载数据文件")
        jh = await get_json()
        logger.info("数据文件下载完成")
        print(jh)
        for items in jh.values():
            name = items["name"]
            url = "https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/img/jinghao_rank/" + name
            img = await get_content(url)
            with open(DATA_PATH + "img/jinghao_rank/" + name, "wb") as f:
                f.write(img)
    else:
        async def download():
            img_url = "https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/img/jinghao_rank/" + name
            img_c = await get_content(img_url, wanted_type="img")
            with open(DATA_PATH + "img/jinghao_rank/" + name, "wb") as f:
                f.write(img_c)
        jh = await get_json()
        for items in jh.values():
            name = items["name"]
            raw_hash = items["hash"]
            try:
                if hashlib.md5(open(DATA_PATH + "img/jinghao_rank/" + name, "rb").read()).hexdigest() == raw_hash:
                    continue
                else:
                    await download()
            except FileNotFoundError:
                await download()