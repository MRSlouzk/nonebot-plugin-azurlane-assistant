# Python Script Created by MRS
from nonebot.adapters.onebot.v11 import Bot, Event, Message, PrivateMessageEvent
from typing import List

# Python Script Created by MRS
import requests as rq
from requests import Session

from .config import config
async def parse(resp: rq.Response) -> dict | str | bytes:
    header = resp.headers.get("content-type")
    if("html" in header):
        resp.encoding="utf-8"
        return resp.text
    elif("json" in header):
        resp.encoding="utf-8"
        return resp.json()
    elif ("image" in header):
        return resp.content
    else:
        resp.encoding="utf-8"
        return resp.text

async def get_content(
        url: str,
        *args,
        timeout: int = 10,
        proxies: dict = None,
        **kwargs
) -> dict | str | bytes:
    """
    获取页面

    :param url:链接
    :param timeout:超时时间
    :param proxies: 代理
    :return:页面内容
    """
    if(proxies is not None):
        resp = rq.get(url, timeout=timeout, proxies=proxies)
    else:
        resp = rq.get(url, timeout=timeout)
    return (await parse(resp))

async def send_forward_msg(
        bot: Bot,
        event: Event,
        name: str,
        uin: str,
        msgs: List[Message]
):
    """
    :说明: `send_forward_msg`
    > 发送合并转发消息
    :参数:
      * `bot: Bot`: bot 实例
      * `event: GroupMessageEvent`: 群聊事件
      * `name: str`: 名字
      * `uin: str`: qq号
      * `msgs: List[Message]`: 消息列表
    """

    def to_node(msg: Message):
        return {"type": "node", "data": {"name": name, "uin": uin, "content": msg}}

    messages = [to_node(msg) for msg in msgs]
    is_private = isinstance(event, PrivateMessageEvent)
    if(is_private):
        await bot.call_api(
            "send_private_forward_msg", user_id=event.user_id, messages=messages
        )
    else:
        await bot.call_api(
            "send_group_forward_msg", group_id=event.group_id, messages=messages
        )