<div align="center">
  <a href="https://wiki.biligame.com/blhx/%E9%A6%96%E9%A1%B5"><img src="https://patchwiki.biligame.com/images/blhx/thumb/e/e9/nlvw0ar5egivnew7tq5oijw4xmf6sbr.png/100px-%E7%A2%A7%E8%93%9D%E8%88%AA%E7%BA%BFicon.png" width="150" height="150"></a>
  <br>
</div>

<div align="center">

# nonebot-plugin-azurlane-assistant

_✨ 基于 NoneBot2 的碧蓝航线辅助插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/MRSlouzk/nonebot-plugin-azurlane-assistant.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-azurlane-assistant">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-azurlane-assistant.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

本插件为游戏“碧蓝航线”的辅助性插件，目前正在开发中，更多功能敬请期待  
本项目所有数据均来自[碧蓝航线wiki](https://wiki.biligame.com/blhx/首页)

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-azurlane-assistant

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-azurlane-assistant
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-azurlane-assistant
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-azurlane-assistant
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-azurlane-assistant
</details>

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('nonebot_plugin_azurlane_assistant')

</details>

<details>
<summary>从 github 安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 输入以下命令克隆此储存库

    git clone https://github.com/MRSlouzk/nonebot-plugin-azurlane-assistant.git

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('src.plugins.nonebot_plugin_assistant')

</details>

## ⚙️ 配置

暂无

## 🎉 使用
### 指令表

暂无

### 效果图

暂无

## 🚧预定计划
### 基础功能
模拟大建（使用纯代码+json数据下载解决）  
舰队编码解码器（类似于wiki的[舰队模拟器](https://wiki.biligame.com/blhx/舰队模拟器?AFLD=&UID=1774065779&name=13（12）船打通全碧蓝&page=A2102B7094E5A6253D2FAE9FDB79B379&type=综合)）  
井号榜查阅  
官方更新推送  

### 进阶功能
各种数据的计算（参考[碧蓝公式合计](https://wiki.biligame.com/blhx/%E5%85%AC%E5%BC%8F%E5%90%88%E9%9B%86)）  
wiki链接跳转
