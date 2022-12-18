# Python Script Created by MRS
name = "nonebot-plugin-azurlane-assistant"

from nonebot import on_command, get_driver
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message, MessageEvent
from nonebot.params import CommandArg
from nonebot.log import logger

from .modules import build_simulator as bs
from .modules.utils import *
from .modules.japan_ship_contrast import japan_ship
from .check_resources import update_res

driver = get_driver()
@driver.on_startup
async def _():
    from httpx._exceptions import TimeoutException
    logger.info("正在更新资源文件...")
    # await update_res()
    # logger.info("资源文件更新完成")
    try:
        await update_res()
        logger.info("资源文件更新完成")
    except TimeoutException:
        logger.error("文件下载超时,请检查代理设置")
    except Exception as e:
        logger.error(e)

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
        await matcher.finish("和谐名:{},中文原名:{},日文拼音:{}".format(info[0], info[1], info[2]))
    else:
        await matcher.finish("参数格式错误,请重新输入")