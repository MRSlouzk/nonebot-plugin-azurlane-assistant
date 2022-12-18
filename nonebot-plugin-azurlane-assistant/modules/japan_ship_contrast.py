# Python Script Created by MRS
import json
from typing import Tuple

async def japan_ship(
        name: str
    ) -> Tuple[str, str, str]:
    """
    重樱船名对照
    :param name:船名
    :return:和谐名,中文原名,拼音
    """
    with open("./data/azurlane/data/japan_ship_name.json", "r", encoding="utf-8") as f:
        cot: dict = json.load(f)
    if(cot.get(name) is None):
        return (name, cot.get(name)["ori"], cot.get(name)["pinyin"])
    else:
        for v in cot.values():
            if(v["ori"] == name):
                return (v["name"], v["ori"], v["pinyin"])
        raise Exception("未找到该船名信息")