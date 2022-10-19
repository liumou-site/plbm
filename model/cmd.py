# -*- encoding: utf-8 -*-
"""
@File    :   CMD.py
@Time    :   2022-09-06 16:16
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   执行系统命令
"""
from os import system, chdir, path, getcwd, getenv
from subprocess import getstatusoutput, getoutput
import platform
from model.logs import logger_init
from logging import getLogger


class Cmd:
	def __init__(self, password: string, cmd: string, terminal: bool, log: bool, work=getcwd()):
		"""
		执行系统指令
		:param terminal: 是否使用图形终端执行, 全局默认,子功能可自定义
		:param password: 主机密码(string)
		:param cmd: 需要执行的命令(string)
		:param log: 是否使用日志打印信息
		:param work: 工作目录(string)
		"""
		self.pwd = getcwd()
		self.logs = log
		chdir(work)
		# 是否使用终端执行
		self.terminal = terminal
		# 设置主机密码
		self.password = password
		# 传入初始命令
		self.cmd = cmd
		# 生成最终命令
		self.cmd_ = None
		# 执行结果
		self.ok = False
		# 终端类型
		self.terminal_type = ''
		# 终端参数
		self.terminal_arg = ''
		# 退出状态码
		self.code = 0
		# home路径
		self.home = getenv('HOME')
		# 临时脚本文件
		self.sh = path.join(self.home, 'run_tmp.sh')
		# 系统类型
		self.os_type = platform.system()
		if str(self.os_type).lower() == 'linux'.lower():
			self.os_type = getoutput("""grep ^ID /etc/os-release | sed 's/ID=//' | sed -n 1p | sed 's#\"##g'""")

		# 初始化日志
		self.logger = getLogger()
		# 定义日志文件
		log_file = os.path.join(self.home, 'cmd_.log')
		logger_init(self.logger, log_file)


	def create(self):
		"""
		创建命令脚本
		:return:
		"""
		try:
			with open(file=self.sh, mode='w+', encoding='utf-8') as w:
				w.write('#!/bin/bash\n')
				w.write(self.cmd_)
				w.close()
		except Exception as e:
			print(e)
		system("chmod +x %s" % self.sh)
		system("cat %s" % self.sh)

	def _get_terminal(self):
		"""
		获取终端类型
		:return:
		"""
		t_ = {'mate-terminal': '-e',
		      'gnome-terminal': '-e',
		      'deepin-terminal': '-C'}
		for i in t_:
			cmd = "which %s" % str(i)
			if int(system(cmd)) == 0:
				self.terminal_type = str(i)
				self.terminal_arg = t_[i]
				return True
		return False

	def terminal_fun(self):
		"""
		使用终端执行命令
		:return:
		"""
		if self._get_terminal():
			cmd = """%s %s '%s;read -p "请按回车关闭此界面"'""" % (self.terminal_type, self.terminal_arg, self.cmd_)
			if self.logs:
				self.logger.debug(cmd)
			else:
				print(cmd)
			getoutput(cmd)
		else:
			print('找不到终端类型,当前系统类型: %s' % self.os_type)

	def shell(self, cmd=None, terminal=None):
		"""
		执行普通Shell命令
		:param terminal: 是否使用终端
		:param cmd: 需要执行的命令，默认使用实例初始命令
		:return: 当使用父进程的时候，返回退出代码
		"""
		if cmd is None:
			cmd = self.cmd
		if terminal is None:
			terminal = self.terminal
		self.cmd_ = cmd
		if self.logs:
			self.logger.debug(self.cmd_)
		else:
			print(self.cmd_)
		if terminal:
			self.terminal_fun()
		else:
			self.code = system(self.cmd_)
			return self.code

	def sudo(self, cmd=None, terminal=None):
		"""
		执行sudo命令
		:param cmd: 需要执行的命令，默认使用实例初始命令
		:return: 当使用父进程的时候，返回退出代码
		"""
		if cmd is None:
			cmd = self.cmd
		if terminal is None:
			terminal = self.terminal
		self.cmd_ = str("""echo %s | sudo -S %s""" % (self.password, cmd))
		if terminal:
			self.terminal_fun()
			return True
		else:
			self.code = system(self.cmd_)
		return False

	def getout(self, cmd=None):
		"""
		获取命令输出
		:param cmd: 需要执行的命令，默认使用实例初始命令
		:return:
		"""
		if cmd is None:
			cmd = self.cmd
		if self.logs:
			self.logger.debug(self.cmd_)
		else:
			print(self.cmd_)
		i = getstatusoutput(cmd)
		self.code = i[0]
		return i[1]

	def getout_sudo(self, cmd=None):
		"""
		获取命令输出
		:param cmd: 需要执行的命令，默认使用实例初始命令
		:return:
		"""
		if cmd is None:
			cmd = self.cmd
		cmd = str("echo %s | sudo -S %s" % (self.password, cmd))
		if self.logs:
			self.logger.debug(cmd)
		else:
			print(cmd)
		i = getstatusoutput(cmd)
		self.code = i[0]
		return i[1]

	def echo_to_file(self, file, cmd):
		"""
		追加echo结果到文件
		:param file: 例如: /etc/sysctl.conf
		:param cmd: 例如: echo 123
		:return:
		"""
		system("echo {0} | sudo -S pwd".format(self.password))
		cmd = str("{0} | sudo tee -a {1}".format(cmd, file))
		self.shell(cmd=cmd, terminal=False)
  
	def add_path(self, paths):
		"""
		追加path路径到用户变量
		:param paths:
		:return:
		"""
		l = getenv("PATH").lower().split(":")
		if str(paths).lower() in l:
			self.logger.debug("Path env is Exists")
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