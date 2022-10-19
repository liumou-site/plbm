# -*- encoding: utf-8 -*-
"""
@File    :   apt.py
@Time    :   2022-09-05 09:17
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
from os import system, getenv, path
from subprocess import getstatusoutput
from logging import getLogger


class Cmd:
	def __init__(self, passwd, debug=False):
		"""

		:param passwd:
		"""
		self.debug = debug
		self.passwd = passwd
		self.result = ""
		self.home = getenv('HOME')

	def sudo(self, cmd, name=None):
		"""

		:param cmd:
		:param name:
		:return:
		"""
		cmd_ = str("echo %s | sudo -S %s" % (self.passwd, cmd))
		return self.shell(cmd_, name=name)

	def shell(self, command, name=None, ):
		"""
		:param command:
		:param name:
		:return:
		"""
		result = []
		if self.debug:
			res = int(system(command))
		else:
			result = getstatusoutput(command)
			res = result[0]
		if int(res) == 0:
			if name:
				logger.info("[ %s ] Success" % name)
			else:
				logger.info("[ %s ] Success" % command)
			return True
		else:
			if name:
				logger.error("[ %s ] Failed" % name)
			else:
				if not self.debug:
					logger.error(result[1])
				logger.error("[ %s ] Failed" % command)
			return False

	def add_path(self, paths):
		"""

		:param paths:
		:return:
		"""
		l = getenv("PATH").lower().split(":")
		if str(paths).lower() in l:
			logger.debug("Path env is Exists")
			return False
		else:
			print("Add [ %s ] To PATH" % paths)
			file = path.join(self.home, '.bashrc')
			try:
				w = open(file=file, mode='w+', encoding='utf8')
				txt_path = str("\nexport PATH=${PATH}:%s" % paths)
				w.write(txt_path)
				w.close()
				return True
			except Exception as e:
				logger.error("add_path: %s " % str(e))
				return False

	def getout_sudo(self, cmd=None):
		"""
		获取命令输出
		:param cmd: 需要执行的命令，默认使用实例初始命令
		:return:
		"""
		if cmd is None:
			cmd = self.cmd
		cmd = str("echo %s | sudo -S %s" % (self.password, cmd))
		i = getstatusoutput(cmd)
		self.code = i[0]
		return i[1]

	def echo_to_file(self, file, cmd):
		"""
		追加echo结果到文件
		:param file: 例如: /etc/sysctl.conf
		:param cmd: 例如：echo 123
		:return:
		"""
		system("echo {0} | sudo -S pwd".format(self.password))
		cmd = str("{0} | sudo tee -a {1}".format(cmd, file))
		self.shell(terminal=False)
