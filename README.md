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

| 配置项        | 必填 | 默认  | 说明                                           |
| ------------- | ---- | ----- | ---------------------------------------------- |
| az_proxy      | no   | false | 是否使用代理(格式:"http://127.0.0.1:7890")     |
| playwright_on | no   | false | 是否启用playwright(若禁用则无法使用舰队模拟器) |

## 🎉 使用
### 指令表

| 前缀       | 参数                | 功能                       |
| ---------- | ------------------- | -------------------------- |
| 模拟建造   | 池子类型 次数       | 抽取模拟建造池             |
| 重樱船名   | 和谐名              | 由和谐名得知其原名以及拼音 |
| 舰队模拟器 | 舰队代码 模拟器类型 | 由舰队代码获取具体舰队     |

(写的不是很详细,后续会完善)

### 效果图

暂无

## 🚧预定计划
### 基础功能
模拟大建
舰队编码解码器（类似于wiki的[舰队模拟器](https://wiki.biligame.com/blhx/舰队模拟器?AFLD=&UID=1774065779&name=13（12）船打通全碧蓝&page=A2102B7094E5A6253D2FAE9FDB79B379&type=综合)）  
井号榜查阅  
官方更新推送(TODO)  

### 进阶功能
各种数据的计算(TODO)  (参考[碧蓝公式合计](https://wiki.biligame.com/blhx/%E5%85%AC%E5%BC%8F%E5%90%88%E9%9B%86)) 
wiki链接跳转

## 🐛 已知问题
1.非windows系统使用建造模拟器会导致截图时出现乱码  
解决方案:先用locale -a确认系统内有"zh_CN",然后安装中文字体(centos:yum groupinstall Fonts)  
2.启动playwright时报错缺少依赖  
解决方案:https://haruka-bot.sk415.icu/faq.html#playwright-%E4%BE%9D%E8%B5%96%E4%B8%8D%E5%85%A8  
3.启动时资源文件无法同步  
解决方案:大多数是因为连接超时所导致的,推荐使用科学上网,后续会考虑制作镜像