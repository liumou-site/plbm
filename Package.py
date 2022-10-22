#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   Package.py
@Time    :   2022-10-23 01:40
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   Linux包管理工具
"""
from apt import AptManager
from dpkg import DpkgManager
from yum import YumManager
from cmd import ComMand
from Jurisdiction import Jurisdiction


class PackageManger:
	def __init__(self, password, logs=True):
		"""
		Linux包管理模块
		:param password: 主机密码
		"""
		self.logs = logs
		self.password = password
		self.cmd = ComMand(password=password, logs=logs)
		self.ju = Jurisdiction(passwd=password, logs=logs)
		self.install_tools = 'apt'
		self.manger = AptManager(password=password, log=logs)
		self.local = DpkgManager(password=password, log=logs)
		if self.cmd.shell(cmd='which yum', terminal=False):
			self.manger = YumManager(password=password, log=logs)
			self.install_tools = 'yum'

	def check_sudo(self):
		"""
		检测是否已有sudo权限
		:return:
		"""
		return self.ju.verification(name='PackageManger - check_sudo')

	def install(self, package, update=False):
		"""
		在线安装服务
		:param update: 是否更新索引再安装
		:param package: 需要安装的包
		:return: 安装结果(bool)
		"""
		return self.manger.install(pac=package, update=update)

	def install_local_file(self, file):
		"""
		安装本地安装包文件
		:param file: 需要安装的文件
		:return: 安装结果(bool)
		"""
		return self.manger.local_install_f(file=file)

	def uninstall(self, package):
		"""
		移除软件包
		:param package: 需要移除的软件名称
		:return:
		"""
		return self.local.uninstall(pac=package)