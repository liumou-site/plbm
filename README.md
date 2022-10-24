# PythonLinuxBasicModule

由于工作中需要编写大量的Linux平台管理脚本、而其中大部分代码都是重复的，所以为了更好的开发效率，我决定将日常Linux管理脚本中用到的基础功能集合起来并使用开源都方式共享，同时也希望有更多人能够一起完善。

## 简介

    [PythonLinuxBasicModule](https://gitcode.net/qq_36154886/PythonLinuxBasicModule)（Python Linux基础模块: `plbm`）是使用Python3进行编写的一个开源系统管理工具，
通过封装Linux系统都软件包管理、磁盘管理、文件管理、网络管理、安全管理、服务管理等内容从而实现快速开发的效果。

后续将加入

* 常用服务快速部署模块


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
git clone https://gitcode.net/qq_36154886/PythonLinuxBasicModule.git
cd plbm
python3 install.py
```

### 安装-作为项目模块

直接进入你的项目根目录,然后执行下面的命令即可

```shell
git clone https://gitcode.net/qq_36154886/PythonLinuxBasicModule.git
cp -rf PythonLinuxBasicModule/plbm .
rm -rf PythonLinuxBasicModule
```



# Demo

```shell
root@liumou-NUC11PAHi5:/home/liumou/LinuxData/git/PythonLinuxBasicModule# tree 
├── demo.py
├── plbm
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

root@liumou-NUC11PAHi5:/home/liumou/LinuxData/git/PythonLinuxBasicModule# cat demo.py 
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
from plbm import *

log = Loger()
log.info('demo')

service = ServiceManagement(service='docker.service', password='1')
service.status()

cmd = ComMand(password='1', cmd='apt update')
cmd.sudo()
root@liumou-NUC11PAHi5:/home/liumou/LinuxData/git/PythonLinuxBasicModule# python3 demo.py 
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
root@liumou-NUC11PAHi5:/home/liumou/LinuxData/git/PythonLinuxBasicModule# 
```