# Python Script Created by MRS
import json

async def find_jinghao_img(num: str) -> bytes:
    data_path = "./data/azurlane/data/jinghao_rank.json"
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