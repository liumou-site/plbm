# LinuxToolsBase

## 简介
LinuxToolsBase（Linux基础工具）是使用Python3进行编写的一个开源系统管理工具，
通过封装Linux系统都包管理、磁盘管理、文件管理、网络管理、安全管理等内容从而实现快速开发的效果。

## 特色

* 使用全中文注释，即使小白也能轻松上手
* 完全使用内置模块进行开发，拿来即用
* 使用Python基础语法进行编写，兼容新旧版本Python3，告别语法冲突(例如3.5及以下版本无法使用f"{}"语法)
* 完全开源、永久免费


# 使用方法

## 安装
### 安装-作为系统/用户模块

> 此方法待发布

```shell
git clone https://gitcode.net/qq_36154886/LinuxToolsBase.git
cd pltb
python3 install.py
```

### 安装-作为项目模块

直接进入你的项目根目录,然后执行下面的命令即可

```shell
git clone https://gitcode.net/qq_36154886/LinuxToolsBase.git
cp -rf LinuxToolsBase/pltb .
rm -rf LinuxToolsBase
```

## 导入

通过`LinuxToolsBase`开始导入，如下

```python
from pltb.cmd import ComMand
from pltb.FileManagement import FileManagement


class NetStatus:
	def __init__(self, ip=None, port=None):
		"""
		网络工具，用于判断网络是否正常
		:param ip: 需要判断的IP
		:param port:  需要判断的端口. Defaults to None.
		"""
		self.ip = ip
		self.port = port
		self.status = False
		#
		self.headers = {}
		self._config()
		self.cmd = ComMand(password='Gxxc@123')
		self.fm = FileManagement()
```


# Demo

```shell
root@liumou-NUC11PAHi5:/home/liumou/LinuxData/git/LinuxToolsBase# tree 
├── demo.py
├── pltb
│   ├── AptManage.py
│   ├── base.py
│   ├── cmd.py
│   ├── dpkg.py
│   ├── FileManagement.py
│   ├── get.py
│   ├── __init__.py
│   ├── Jurisdiction.py
│   ├── logger.py
│   ├── NetManagement.py
│   ├── NetStatus.py
│   ├── Package.py
│   ├── pacman.py
│   ├── README.md
│   ├── Service.py
│   ├── setup.py
│   ├── source.py
│   └── yum.py

root@liumou-NUC11PAHi5:/home/liumou/LinuxData/git/LinuxToolsBase# cat demo.py 
# -*- encoding: utf-8 -*-
"""
@File    :   demo.py
@Time    :   2022-10-24 22:45
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
from pltb import *

log = Loger()
log.info('demo')

service = ServiceManagement(service='docker.service', password='1')
service.status()

cmd = ComMand(password='1', cmd='apt update')
cmd.sudo()
root@liumou-NUC11PAHi5:/home/liumou/LinuxData/git/LinuxToolsBase# python3 demo.py 
2022-10-24 23:11:08 logger - logger.py : line: 83 - INFO : demo
找不到终端程序: 
/usr/bin/gnome-terminal
存在终端程序: gnome-terminal
2022-10-24 23:11:08 cmd - cmd.py : line: 205 - DEBUG : echo 1 | sudo -S systemctl -all | grep docker.service | awk '{print $4}'
2022-10-24 23:11:08 cmd - cmd.py : line: 205 - DEBUG : echo 1 | sudo -S systemctl -all | grep docker.service | awk '{print $4}'
2022-10-24 23:11:08 cmd - cmd.py : line: 205 - DEBUG : echo 1 | sudo -S systemctl -all | grep docker.service | awk '{print $4}'
2022-10-24 23:11:08 cmd - cmd.py : line: 205 - DEBUG : echo 1 | sudo -S systemctl -all | grep docker.service | awk '{print $4}'
[ docker.service ] 执行成功
找不到终端程序: 
/usr/bin/gnome-terminal
存在终端程序: gnome-terminal
命中:1 https://mirrors.ustc.edu.cn/ubuntu jammy InRelease
命中:2 https://mirrors.ustc.edu.cn/ubuntu jammy-updates InRelease
命中:3 https://mirrors.ustc.edu.cn/ubuntu jammy-backports InRelease
命中:4 https://mirrors.ustc.edu.cn/ubuntu jammy-security InRelease
正在读取软件包列表... 完成
正在分析软件包的依赖关系树... 完成
正在读取状态信息... 完成                 
有 56 个软件包可以升级。请执行 ‘apt list --upgradable’ 来查看它们。
[ apt update ] 执行成功
root@liumou-NUC11PAHi5:/home/liumou/LinuxData/git/LinuxToolsBase# 
```