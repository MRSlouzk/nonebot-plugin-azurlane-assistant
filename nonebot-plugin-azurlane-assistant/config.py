# Python Script Created by MRS
from typing import Optional

from nonebot import get_driver
from pydantic import BaseModel

class Config(BaseModel):
    az_proxy: Optional[str] = None
    playwright_on :Optional[bool] = False

config = Config.parse_obj(get_driver().config.dict())