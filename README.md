<div align="center">
  <a href="https://wiki.biligame.com/blhx/%E9%A6%96%E9%A1%B5"><img src="https://patchwiki.biligame.com/images/blhx/thumb/e/e9/nlvw0ar5egivnew7tq5oijw4xmf6sbr.png/100px-%E7%A2%A7%E8%93%9D%E8%88%AA%E7%BA%BFicon.png" width="150" height="150"></a>
  <br>
</div>

<div align="center">

# nonebot-plugin-azurlane-assistant

_✨ NoneBot 插件简单描述 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/MRSlouzk/nonebot-plugin-azurlane-assistant.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-azurlane-assistant">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-azurlane-assistant.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

这是一个 nonebot2 插件项目的模板库, 你可以直接使用本模板创建你的 nonebot2 插件项目的仓库

模板库使用方法:
1. 点击仓库中的 "Use this template" 按钮, 输入仓库名与描述, 点击 "  Create repository from template" 创建仓库
2. 在创建好的新仓库中, 在 "Add file" 菜单中选择 "Create new file", 在新文件名处输入`LICENSE`, 此时在右侧会出现一个 "Choose a license template" 按钮, 点击此按钮选择开源协议模板, 然后在最下方提交新文件到主分支
3. 全局替换`owner`为仓库所有者ID; 全局替换`nonebot-plugin-example`为插件名; 全局替换`nonebot_plugin_example`为包名; 修改 python 徽标中的版本为你插件的运行所需版本
4. 修改 README 中的插件名和插件描述, 并在下方填充相应的内容

## 📖 介绍

这里是插件的详细介绍部分

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

    poetry add nonebot-plugin-example
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

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| 配置项1 | 是 | 无 | 配置说明 |
| 配置项2 | 否 | 无 | 配置说明 |

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 指令1 | 主人 | 否 | 私聊 |配置说明 |
| 指令2 | 群员 | 是 | 群聊 |配置说明 |
### 效果图
如果有效果图的话
