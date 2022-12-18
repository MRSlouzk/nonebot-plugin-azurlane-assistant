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
    if(cot.get(name) is not None):
        return (name, cot.get(name)["ori"], cot.get(name)["pinyin"])
    else:
        for v in cot.keys():
            if(cot.get(v)["ori"] == name):
                return (v, cot.get(v)["ori"], cot.get(v)["pinyin"])
        raise Exception("未找到该船名信息")