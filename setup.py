from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='nonebot-plugin-azurlane-assistant',
    version='0.0.1',
    packages=['nonebot-plugin-azurlane-assistant'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MRSlouzk/nonebot-plugin-azurlane-assistant/',
    license='MIT',
    author='MRSlouzk',
    author_email='mrslouzk@qq.com',
    description='碧蓝航线辅助插件'
)
