from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='nonebot-plugin-azurlane-assistant',
    version='0.0.2',
    packages=['nonebot-plugin-azurlane-assistant', 'nonebot-plugin-azurlane-assistant.modules'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MRSlouzk/nonebot-plugin-azurlane-assistant/',
    license='MIT',
    author='MRSlouzk',
    author_email='mrslouzk@qq.com',
    description='碧蓝航线辅助插件',
    install_requires=['nonebot-adapter-onebot>=2.0.0-beta.2,<3.0.0', 'nonebot2>=2.0.0-beta.1,<3.0.0', 'httpx>=0.23.1', 'playwright>=1.28.0'],
)
