# -*- encoding: utf-8 -*-
"""
@File    :   dpkg.py
@Time    :   2022-09-05 09:17
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
from model.cmd import Cmd


class Apt:
	def __init__(self, passwd, debug=False):
		"""
		Apt Manger
		:param passwd:
		"""
		self.passwd = passwd
		self.cmd = Cmd(passwd=passwd, debug=debug)

	def install(self, deb_file='git'):
		"""

		:param deb_file:
		:return:
		"""
		print("Installing %s ..." % deb_file)
		cmd = str("dpkg -i %s" % deb_file)
		return self.cmd.sudo(cmd=cmd, name='Install %s' % deb_file)

	def configure(self):
		"""
		:return:
		"""
		return self.cmd.sudo(cmd="dpkg --configure -a")

	def uninstall(self, pac, name=None):
		"""

		:param name:
		:param pac:
		:return:
		"""
		cmd = str("dpkg -P %s" % pac)
		if name is None:
			name = 'UnInstall %s' % pac
		print("UnInstalling %s ..." % name)
		return self.cmd.sudo(cmd=cmd, name=name)