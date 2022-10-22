#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   yum.py
@Time    :   2022-10-23 01:41
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   Yum包管理工具
"""

from cmd import ComMand


class YumManager:
	def __init__(self, password, log=False, terminal=False):
		"""
		yum 管理
		:param password: 主机密码
		:param log: 是否启用日志
		:param terminal: 是否使用终端执行命令(针对个别Linux发行部才起作用)
		"""
		self.terminal = terminal
		self.log = log
		self.password = password
		self.cmd = ComMand(password=self.password, cmd='which yum', terminal=self.terminal, log=self.log)

	def install(self, pac='git', update=False):
		"""
		安装在线包
		:param update: 是否更新源索引(默认不会更新源索引)
		:param pac: 需要安装的包(字符串)
		:return:
		"""
		if update:
			self.update_index()
		print("Installing %s ..." % pac)
		cmd = str("yum install -y %s" % pac)
		return self.cmd.sudo(cmd=cmd, name='Install %s' % pac)

	def update_index(self):
		"""
		更新源索引
		:return:
		"""
		return self.cmd.sudo(cmd="yum clean all;yum makecache", name="Update Sources")

	def local_install_f(self, file):
		"""
		实现yum install -y -f ./install.deb的效果
		:param file:
		:return:
		"""
		return self.cmd.sudo(cmd="yum install -y -f %s" % file, name='Install Local Package')

	def reinstall_rc(self, update=False):
		"""
		一键修复 rc 状态的包列表
		:param update: 是否更新源索引(默认不会更新源索引)
		:return:执行结果(bool)
		"""
		if update:
			self.update_index()
		cmd = "yum install -y --reinstall `rpm -l | grep -v ii  | grep rc | awk '{print $2}' | sed '1,5 d'`"
		return self.cmd.sudo(cmd=cmd, name='List of packages to repair rc status', terminal=False)

	def remove_rc(self, update=False):
		"""
		一键卸载 rc 状态的包列表
		:param update: 是否更新源索引(默认不会更新源索引)
		:return:执行结果(bool)
		"""
		if update:
			self.update_index()
		cmd = "yum remove -y `rpm -l | grep -v ii  | grep rc | awk '{print $2}' | sed '1,5 d'`"
		return self.cmd.sudo(cmd=cmd, name='List of packages in unloaded rc status', terminal=False)

	def update(self, update=True):
		"""
		更新系统
		:param update: 是否更新源索引(默认不会更新源索引)
		:return:
		"""
		if update:
			self.update_index()
		cmd = 'yum update -y'
		return self.cmd.sudo(cmd=cmd, terminal=False, name='更新系统-upgrade')