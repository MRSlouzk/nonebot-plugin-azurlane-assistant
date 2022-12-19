# Python Script Created by MRS
from typing import Optional

from nonebot.permission import SUPERUSER
from playwright.async_api import Browser, Playwright

name = "nonebot-plugin-azurlane-assistant"

from nonebot import on_command, get_driver
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message, MessageEvent, MessageSegment
from nonebot.params import CommandArg
from nonebot.log import logger

from .modules import build_simulator as bs
from .modules.utils import *
from .modules.japan_ship_contrast import japan_ship
from .modules.jinghao import find_jinghao_img, get_mapping_jh

from .check_resources import update_res
from .config import config
from .brower import start, shut, open_ship_fleet_simulator

driver = get_driver()
_brower: Optional[Browser] = None
_playwright: Optional[Playwright] = None
@driver.on_startup
async def _():
    from httpx._exceptions import TimeoutException
    logger.info("正在更新资源文件...")
    try:
        await update_res()
        logger.info("资源文件更新完成")
    except TimeoutException:
        logger.error("文件下载超时,请检查代理设置")
        return
    except Exception as e:
        logger.error(e)
        return

    if(config.playwright_on):
        global _brower, _playwright
        logger.info("正在启动playwright...")
        try:
            (_brower, _playwright) = await start()
        except Exception as e:
            logger.error(e)
    else:
        logger.warning("配置文件中已禁用playwright, 会导致\"舰队模拟器\"等功能无法使用")

@driver.on_shutdown
async def _():
    if(config.playwright_on):
        logger.info("正在关闭playwright...")
        global _playwright, _brower
        try:
            await shut(_brower, _playwright)
        except Exception as e:
            logger.error(e)
            logger.warning("playwright关闭失败!若卡死请直接kill本进程")

@on_command("井号榜").handle()
async def _(matcher: Matcher ,arg: Message = CommandArg()):
    args = arg.extract_plain_text().split()
    if(len(args)==0):
        await matcher.finish("请输入>>井号榜 help<<查看具体用法")
    elif(len(args) == 1):
        if(args[0] == "help"):
            msg = Message("序号表\n")
            lst = await get_mapping_jh()
            for i in lst:
                msg += Message(f"{i[0]}:{i[1]}\n")
            await matcher.finish(msg)
        else:
            try:
                img = await find_jinghao_img(args[0])
                await matcher.finish(MessageSegment.image(img))
            except Exception as e:
                await matcher.finish(str(e))
    else:
        await matcher.finish("参数错误,请输入>>井号榜 help<<查看具体用法")

@on_command("模拟建造").handle()
async def _(bot: Bot, event: MessageEvent,matcher: Matcher ,arg: Message = CommandArg()):
    async def pool_type(cn_name: str, matcher0: Matcher) -> str:
        if (cn_name == "轻型"):
            return "qx"
        elif (cn_name == "重型"):
            return "zx"
        elif (cn_name == "特型"):
            return "tx"
        elif (cn_name == "限时"):
            # return "xd"
            await matcher0.finish("目前暂不支持限时池抽取")
        else:
            await matcher0.finish("参数错误，仅支持轻型/重型/特型/限时池")
    args = arg.extract_plain_text().split()
    b_type, times = "qx", 1
    if(len(args)==0):
        await matcher.finish("大建模拟器使用方法\n(池子数据来源为碧蓝航线wiki)\n*所有指令均需要指令前缀\n>>模拟建造<<：显示本菜单\n>>模拟建造 轻型/重型/特型/限时<<：单次抽取某池子\n>>模拟建造 轻型/重型/特型/限时 次数<<：抽取[次数]次某池子")
    elif(len(args)==1):
        b_type = await pool_type(args[0], matcher)
    elif(len(args)==2):
        b_type = await pool_type(args[0], matcher)
        if(not str(args[1]).isdigit()):
            await matcher.finish("大建次数必须为整数")
        else:
            if(int(args[1]) <=0 or int(args[1]) > 10):
                await matcher.finish("大建次数超出范围，范围为1-10")
            times = int(args[1])
    else:
        await matcher.finish("参数过多")
    res = await bs.build_simulate(b_type, times=times)
    # print(res)
    msg_lst: List[Message] = []
    times = 0
    for ship in res:
        times = times + 1
        sname = ship.get("name")
        quality = ship.get("quality")
        msg_lst.append(Message(f"第{times}次抽取\n名称:{sname}\n品质:{quality}"))
    msg_lst.append(Message("池子数据均来自碧蓝航线wiki\nhttps://wiki.biligame.com/blhx/%E5%BB%BA%E9%80%A0%E6%A8%A1%E6%8B%9F%E5%99%A8"))
    await send_forward_msg(bot, event, "大建模拟器", bot.self_id, msg_lst)

@on_command("搜索页面跳转").handle()
async def _(matcher: Matcher,arg: Message = CommandArg()):
    args = arg.extract_plain_text().split()
    if(len(args)==0):
        await matcher.finish("请输入要搜索的内容")
    elif(len(args)==1):
        cot = args[0]
        await matcher.finish("https://searchwiki.biligame.com/blhx/index.php?search=" + cot + "&go=%E5%89%8D%E5%BE%80")
    else:
        await matcher.finish("一次只能查询一个")

@on_command("重樱船名").handle()
async def _(matcher: Matcher,arg: Message = CommandArg()):
    args = arg.extract_plain_text().split()
    if(len(args)==0):
        await matcher.finish("用法:>>重樱船名 和谐名,中文原名<<, 输出:对应中文原名/和谐名与拼音")
    elif(len(args)==1):
        try:
            info: tuple = await japan_ship(args[0])
        except Exception as e:
            await matcher.finish(str(e))
        await matcher.finish("和谐名:{},中文原名:{},和谐名拼音:{}".format(info[0], info[1], info[2]))
    else:
        await matcher.finish("参数格式错误,请重新输入")

@on_command("舰队模拟器", permission=SUPERUSER).handle()
async def _(matcher: Matcher,arg: Message = CommandArg()):
    args = arg.extract_plain_text().split()
    global _brower
    if(len(args) == 0):
        await matcher.finish(
            "用法:>>舰队模拟器 生成编码 [模拟器种类(bwiki或x94fujo6rpg)]<<, 输出:舰队模拟器结果\n注意:舰队模拟器目前因为技术原因仅支持bwiki生成的,x94fujo6rpg的因为一些技术性问题适配有一定难度(两者代码不通用)")
    elif(len(args) == 1):
        try:
            img = await open_ship_fleet_simulator(_brower, args[0])
            await matcher.finish(MessageSegment.image(img))
        except Exception as e:
            await matcher.finish(str(e))
    elif(len(args) == 2):
        try:
            img = await open_ship_fleet_simulator(_brower, args[0], simulator_type=args[1])
            await matcher.finish(MessageSegment.image(img))
        except Exception as e:
            await matcher.finish(str(e))
    else:
        await matcher.finish(
            "用法:>>舰队模拟器 生成编码 [模拟器种类(bwiki或x94fujo6rpg)]<<, 输出:舰队模拟器结果\n注意:舰队模拟器目前因为技术原因仅支持bwiki生成的,x94fujo6rpg的因为一些技术性问题适配有一定难度(两者代码不通用)")