# LinuxToolsBase

## 简介
LinuxToolsBase（Linux基础工具）是使用Python3进行编写的一个开源系统管理工具，
通过封装Linux系统都包管理、磁盘管理、文件管理、网络管理、安全管理等内容从而实现快速开发的效果。

## 特色

* 使用全中文注释，即使小白也能轻松上手
* 完全使用内置模块进行开发，拿来即用
* 使用Python基础语法进行编写，兼容新旧版本Python3，告别语法冲突(例如3.5及以下版本无法使用f"{}"语法)
* 完全开源、永久免费

## 功能列表

* 软件管理: 弱化原生`apt`、`yum`、`dpkg`、`rpm`等工具的使用差异，在此基础上封装为`package`功能进行管理
* 命令功能：提供`普通权限`、`sudo`权限等接口
* 权限验证：提供基本的Linux普通用户`sudo`权限验证功能,并针对`Uos`增加开发者权限检测功能
* 日志输出：默认提供日志功能
* 网络管理：提供`http`访问状态、`icmp`访问状态判断
* 网络设备：通过网络连接管理，局域网IP检测
* 文件管理：提供文件/文件夹增删改查基本功能



# 使用方法

## 安装

### 安装-作为系统/用户模块


```shell
git clone https://gitcode.net/qq_36154886/LinuxToolsBase.git
cd LinuxToolsBase
python3 install.py
```
### 安装-作为项目模块

直接进入你的项目根目录,然后执行下面的命令即可

```shell
git clone https://gitcode.net/qq_36154886/LinuxToolsBase.git
```

## 导入

通过`LinuxToolsBase`开始导入，如下


```python
from LinuxToolsBase.cmd import ComMand
from LinuxToolsBase.FileManager import FileManager


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
		self.fm = FileManager()
```