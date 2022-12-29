# Python Script Created by MRS
from typing import List, Tuple

from nonebot.log import logger

import os, json
import hashlib
from pathlib import Path, PurePath

from .utils import get_content

DATA_PATH = "./data/azurlane/"

class ResouceChecker(object):
    url_suffix = "https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/"
    data_path = "./data/azurlane/"
    def __init__(self):
        pass

    @classmethod
    def load_json(cls, path: Path) -> dict:
        if(not os.path.exists(path)): pass
        with open(cls.data_path + str(path), "r", encoding="utf-8") as f:
            cot = json.load(f)
        return cot

    @classmethod
    def write_json(cls, path: Path, data: dict = None):
        if data is None:
            data = {}
        with open(cls.data_path + str(path), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def download_imgs(
            cls,
            url: str | List[str],
            *args,
            mode: str = "stream",
            path: Path | PurePath,
            name: str | List[str] = "1.png"
    ) -> List[bytes] | List[Path]:
        """
        图片下载

        :param url: 图片链接/图片链接列表
        :param path: 图片下载路径
        :param mode: 图片下载方式，stream为流式下载，file为文件下载
        :param name: 图片名称
        :return:
        """
        ret_lst, name_lst = [], []
        if isinstance(url, str):
            url = [url]
        if isinstance(name, str):
            name_lst = [name]
        index = 0
        for img_url in url:
            img_c = await get_content(cls.url_suffix + img_url, wanted_type="img")
            if(img_c is None):
                raise Exception("图片下载失败")

            if mode == "stream":
                ret_lst.append(img_c)
            elif mode == "file":
                with open(cls.data_path + str(path) + name_lst[index], "wb") as f:
                    f.write(img_c)
                ret_lst.append(Path(cls.data_path + str(path) + name_lst[index]))
                if(isinstance(name, list)): index += 1
            else:
                raise Exception("未知的下载模式")

        return ret_lst

    @classmethod
    def update_data(
            cls,
            url: str,
            *args,
            mode: str = "stream",
            path: Path | PurePath = "./data/azurlane/1.json",
            is_return: bool = True,
            verify_size = True
    ) -> dict | bool | Tuple[dict, bool] | None:
        """
        下载数据

        :param url: 数据链接地址
        :param mode: 下载模式(流式下载/文件下载), 默认为流式下载, 会返回数据
        :param path: 文件下载的保存路径
        :param is_return: 文件下载时是否返回数据
        :param verify_size: 是否验证文件内容是否相同并返回
        :return:
        """

        data: dict = await get_content(cls.url_suffix + "data/" + url , wanted_type="json")
        if(mode == "stream"): return data
        elif(mode == "file"):
            if(os.path.exists(cls.data_path + str(path))):
                with open(cls.data_path + str(path), "r", encoding="utf-8") as f:
                    old_data = json.load(f)
                if(old_data == data):
                    cot_equ = True
                else:
                    cot_equ = False

                if (verify_size and is_return): return (data, cot_equ)
                elif (verify_size): return cot_equ
                elif (is_return): return data
                return
            with open(cls.data_path + str(path), "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            if(verify_size and is_return): return (data, False)
            elif(verify_size): return False
            elif(is_return): return data
            return
        else:
            raise Exception("未知的下载模式")

    @classmethod
    def check_and_create_paths(cls):
        if(os.path.exists(cls.data_path)):
            return
        logger.warning("资源文件夹不存在，正在创建...")
        os.makedirs(cls.data_path)
        os.makedirs(cls.data_path + "data/")
        os.makedirs(cls.data_path + "img/jinghao_rank")

    @classmethod
    def hash_verify(cls, file_path: Path, hash_file: Path) -> bool | List[Path]:
        """
        文件哈希值校验

        :param file_path: 文件路径
        :param hash_file: 哈希效验文件
        :return:
        """
        file_path = Path(cls.data_path + str(file_path))
        hash_file = Path(cls.data_path + str(hash_file))
        with hash_file.open("r", encoding="utf-8") as f:
            hash_dict: dict = json.load(f)
        if(len(hash_dict.keys()) != len(os.listdir(file_path))):
            raise Exception("文件数量与哈希值数量不匹配")
        update_lst = []
        for i in file_path.iterdir():
            if i.is_dir(): continue
            for v in hash_dict.values():
                if v["name"] == str(i):
                    with i.open("rb") as f:
                        md5 = hashlib.md5(f.read()).hexdigest()
                    if md5 != v["hash"]:
                        update_lst.append(i)
                    break

        if not update_lst:
            return True
        else:
            return update_lst

async def check_resources():
    logger.info("======开始检查资源文件======")
    rc = ResouceChecker() # 导入资源检查类
    rc.check_and_create_paths() #检查并创建资源文件夹

    logger.debug("-----开始更新数据文件-----")
    jinghao = rc.update_data("jinghao_rank.json", path=PurePath("data/jinghao_rank.json"), mode="file")
    pool = rc.update_data("pool.json", path=PurePath("data/pool.json"), mode="file", is_return=False)
    jsn = rc.update_data("japan_ship_name.json", path=PurePath("data/japan_ship_name.json"), mode="file", is_return=False)
    sicon = rc.update_data("ship_icon.json", path=PurePath("data/ship_icon.json"), mode="file")
    if(not jinghao[1]):
        logger.debug("---开始更新井号榜---")
        pathname_lst = []
        name_lst = []
        for items in jinghao[0].values():
            name = items["name"]
            name_lst.append(name)
            pathname_lst.append("img/jinghao_rank/" + name)

        rc.download_imgs(pathname_lst, mode="file", path=PurePath("img/jinghao_rank/"), name=name_lst)
        logger.debug("---井号榜更新完成---")
    else:
        logger.debug("---开始井号榜哈希效验---")
        res = rc.hash_verify(file_path=Path("img/jinghao_rank/"), hash_file=Path("data/jinghao_rank.json"))
        if(res): logger.debug("---井号榜哈希效验通过---")
        else:
            for items in res:
                rc.download_imgs(items, mode="file", path=PurePath("img/jinghao_rank/"), name=items.name)
            logger.debug("---井号榜哈希效验不通过，已更新---")
    if(jinghao[1] and pool and jsn and sicon[1]):
        logger.debug("其余数据文件无须更新~")
        return

    logger.info("======资源文件检查无误======")

# async def update_res():
#     async def get_json(icon_num: int):
#         jinghao: str = await get_content("https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/data/jinghao_rank.json")
#         build_pool: str = await get_content("https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/data/pool.json")
#         japan_ship: str = await get_content("https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/data/japan_ship_name.json")
#         ship_icon: str = await get_content("https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/data/ship_icon.json")
#         (jinghao, build_pool, japan_ship, ship_icon) = json.loads(jinghao), json.loads(build_pool), json.loads(japan_ship), json.loads(ship_icon)
#         jinghao: dict
#         ship_icon: dict
#
#         with open(DATA_PATH + "data/jinghao_rank.json", "w", encoding="utf-8") as f0:
#             json.dump((jinghao), f0, ensure_ascii=False, indent=4)
#         with open(DATA_PATH + "data/pool.json", "w", encoding="utf-8") as f1:
#             json.dump(build_pool, f1, ensure_ascii=False, indent=4)
#         with open(DATA_PATH + "data/japan_ship_name.json", "w", encoding="utf-8") as f2:
#             json.dump(japan_ship, f2, ensure_ascii=False, indent=4)
#         if(ship_icon["num"] != icon_num):
#             with open(DATA_PATH + "data/ship_icon.json", "w", encoding="utf-8") as f2:
#                 json.dump(ship_icon, f2, ensure_ascii=False, indent=4)
#         return jinghao
#
#     if(not os.path.exists(DATA_PATH)):
#         logger.warning("资源文件夹不存在，正在创建...")
#         os.makedirs(DATA_PATH)
#         os.makedirs(DATA_PATH + "data/")
#         os.makedirs(DATA_PATH + "img/jinghao_rank")
#
#         logger.info("开始下载数据文件")
#         with open(DATA_PATH + "data/ship_icon.json", "r", encoding="utf-8") as f:
#             cot = json.load(f)
#         jh = await get_json(int(cot["num"]))
#         logger.info("数据文件下载完成")
#
#         for items in jh.values():
#             name = items["name"]
#             url = "https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/img/jinghao_rank/" + name
#             img = await get_content(url)
#             with open(DATA_PATH + "img/jinghao_rank/" + name, "wb") as f:
#                 f.write(img)
#     else:
#         async def download_jinghao():
#             img_url = "https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/img/jinghao_rank/" + name
#             img_c = await get_content(img_url, wanted_type="img")
#             with open(DATA_PATH + "img/jinghao_rank/" + name, "wb") as f:
#                 f.write(img_c)
#         async def download_icons():
#             icon_url = "https://raw.githubusercontent.com/MRSlouzk/nonebot-plugin-azurlane-assistant-data/main/data/ship_icon.json"
#             icon_c = await get_content(icon_url)
#             with open(DATA_PATH + "data/ship_icon.json", "w", encoding="utf-8") as f:
#                 json.dump(json.loads(icon_c), f, ensure_ascii=False, indent=4)
#
#         logger.info("开始下载数据文件")
#         with open(DATA_PATH + "data/ship_icon.json", "r", encoding="utf-8") as f:
#             cot = json.load(f)
#         jh = await get_json(int(cot["num"]))
#         logger.info("数据文件下载完成")
#
#         for items in jh.values():
#             name = items["name"]
#             raw_hash = items["hash"]
#             try:
#                 if hashlib.md5(open(DATA_PATH + "img/jinghao_rank/" + name, "rb").read()).hexdigest() == raw_hash:
#                     continue
#                 else:
#                     await download_jinghao()
#             except FileNotFoundError:
#                 await download_jinghao()