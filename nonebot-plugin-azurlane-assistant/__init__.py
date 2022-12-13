# Python Script Created by MRS
name = "nonebot-plugin-azurlane-assistant"

from nonebot import on_regex, on_message, on_keyword, on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message, MessageSegment, Event, MessageEvent, GroupMessageEvent
from nonebot.permission import SUPERUSER
from nonebot.params import CommandArg

from .modules import build_simulator as bs
from .utils import *

@on_command("井号榜").handle()
async def _(matcher: Matcher ,arg: Message = CommandArg()):
    args = arg.extract_plain_text().split()
    if(len(args)==0):
        await matcher.finish("")

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
        name = ship.get("name")
        quality = ship.get("quality")
        msg_lst.append(Message(f"第{times}次抽取\n名称:{name}\n品质:{quality}"))
    msg_lst.append(Message("池子数据均来自碧蓝航线wiki\nhttps://wiki.biligame.com/blhx/%E5%BB%BA%E9%80%A0%E6%A8%A1%E6%8B%9F%E5%99%A8"))
    await send_forward_msg(bot, event, "大建模拟器", bot.self_id, msg_lst)