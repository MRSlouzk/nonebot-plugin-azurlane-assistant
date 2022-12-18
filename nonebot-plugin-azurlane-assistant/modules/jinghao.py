# Python Script Created by MRS
import json
from typing import List, Tuple

data_path = "./data/azurlane/data/jinghao_rank.json"
async def find_jinghao_img(num: str) -> bytes:
    img_path = "./data/azurlane/img/"
    with open(data_path, "r", encoding="utf-8") as f:
        cot: dict = json.load(f)
    val = cot.get("img"+num)
    if val is None:
        raise Exception("未找到该编号({})对应图片".format(num))
    else:
        try:
            with open(img_path + val["name"], "rb") as f1:
                img = f1.read()
        except FileNotFoundError:
            raise Exception("资源读取失败,请确认是否成功下载所需资源")
        return img

async def get_mapping_jh() -> List[Tuple[str, str]]:
    with open(data_path, "r", encoding="utf-8") as f:
        cot: dict = json.load(f)
    mapping_lst = []
    for i in cot.keys():
        val: dict = cot.get(i)
        name: str = val["name"]
        name = name.split(".")[0]
        i = i.replace("img", "")
        mapping_lst.append((i, name))
    return mapping_lst