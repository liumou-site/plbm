# -*- encoding: utf-8 -*-
"""
@File    :   DPKG.py
@Time    :   2022-09-05 09:17
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
from pltb.cmd import ComMand
from os import path


class DpkgManagement:
	def __init__(self, password, log=False, terminal=False):
		"""
		Apt 管理
		:param password: 主机密码
		:param log: 是否启用日志
		:param terminal: 是否使用终端执行命令(针对个别Linux发行部才起作用)
		"""
		self.log = log
		self.terminal = terminal
		self.password = password
		self.cmd = ComMand(password=self.password, cmd='which apt', terminal=self.terminal, logs=self.log)
		# 需要安装的安装包文件信息
		self.file_install = ''
		# 可安装的文件列表
		self.install_list = []
		# 格式错误的文件列表
		self.format_err = []
		# 不存在的文件列表
		self.not_err = []

	def _show(self):
		"""
		显示信息
		:return:
		"""
		if self.install_list:
			print('可安装的文件列表如下')
			for i in self.install_list:
				print(i)
		if self.format_err:
			print('格式错误的文件列表如下')
			for i in self.format_err:
				print(i)
		if self.not_err:
			print('不存在的文件列表如下')
			for i in self.not_err:
				print(i)

	def _add_file(self, file):
		"""
		检测并添加文件
		:param file:
		:return:
		"""
		f_name = str(file).split('.')[-1]
		if str(f_name).lower() == 'deb':
			if path.isfile(file):
				self.file_install = str(self.file_install) + str(file)
				self.install_list.append(file)
			else:
				print('列表中检测到不存在的安装包: %s' % str(file))
				self.not_err.append(file)
		else:
			print('列表中检测到格式不正确的文件: %s' % str(file))
			self.format_err.append(file)

	def install(self, deb_file=None, name=None):
		"""
		安装本地安装包文件
		:param name: 任务名称
		:param deb_file:传入需要安装的deb文件路径(建议绝对路径),多个文件请使用列表传入
		:return:
		"""
		self.install_list = []
		file = ''
		if type(deb_file) == list:
			for i in deb_file:
				self._add_file(file=i)
		else:
			if type(deb_file) == str:
				self._add_file(file=deb_file)
		if self.install_list:
			print("Installing %s ..." % self.file_install)
			cmd = str("dpkg -i %s" % self.file_install)
			if name is None:
				name = 'Install %s Packages' % len(self.install_list)
			return self.cmd.sudo(cmd=cmd, name=name)
		else:
			print('没有找到可安装的文件信息')
			self._show()

	def configure(self):
		"""
		:return:
		"""
		return self.cmd.sudo(cmd="dpkg --configure -a", name='Continue configuring all Packages')

	def uninstall(self, pac, name=None):
		"""

		:param name: 任务名称
		:param pac:需要卸载的包，例如：docker.io
		:return:
		"""
		cmd = str("dpkg -P %s" % pac)
		if name is None:
			name = 'UnInstall %s' % pac
		print("UnInstalling %s ..." % name)
		return self.cmd.sudo(cmd=cmd, name=name)
