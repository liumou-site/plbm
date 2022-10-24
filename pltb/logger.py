#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   logger.py
@Time    :   2022-10-19 16:01
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
from logging import Formatter, getLogger, StreamHandler, FileHandler
from pltb.base import home_dir
from os import path


class Loger:
	def __init__(self, file=None, console=True, journal=False, bl=None, cl=None, jl=None, bf=None, df=None):
		"""
		初始化日志模块
		:param file: 设置日志文件
		:param console: 是否在控制台显示信息(默认显示)
		:param journal: 是否记录日志到文件
		:param bl: 基本等级,默认 DEBUG
		:param cl: 控制台最低显示级别,默认 DEBUG
		:param jl: 文本日志记录最低级别, 默认 INFO
		:param bf: 基本格式,默认 %(asctime)s %(module)s - %(filename)s : line: %(lineno)s - %(levelname)s : %(message)s
		:param df: 时间格式,默认 %Y-%m-%d %H:%M:%S
		"""
		if bl is None:
			bl = 'DEBUG'
		if cl is None:
			cl = 'DEBUG'
		if jl is None:
			jl = 'INFO'
		if bf is None:
			bf = "%(asctime)s %(module)s - %(filename)s : line: %(lineno)s - %(levelname)s : %(message)s"
		if df is None:
			df = '%Y-%m-%d %H:%M:%S'
		self.basic_level = bl
		self.journal_level = jl
		self.console_level = cl
		self.journal = journal
		self.console = console
		if file is None:
			file = path.join(home_dir, 'pltb.log')
		self.file = file
		self.logger = getLogger()
		self.basic_format = bf
		self.date_format = df
		self.logger.setLevel(self.basic_level)
		self.formatter = Formatter(self.basic_format, self.date_format)
		self.config_console()
		if self.journal:
			self.config_txt()

	def config_console(self):
		"""
		配置控制台终端信息
		:return:
		"""
		c = StreamHandler()  # 输出到控制台的handler
		c.setFormatter(self.formatter)
		c.setLevel(self.console_level)  # 也可以不设置，不设置就默认用logger的level
		self.logger.addHandler(c)

	def config_txt(self):
		"""
		初始化日志
		:return:
		"""
		f = FileHandler(self.file)  # 输出到文件的handler
		print(self.file)
		f.setFormatter(self.formatter)
		self.logger.addHandler(f)

	def info(self, msg):
		"""
		打印信息
		:param msg: 打印内容
		:return:
		"""
		self.logger.info(str(msg))

	def debug(self, msg):
		"""
		打印信息
		:param msg: 打印内容
		:return:
		"""
		self.logger.debug(str(msg))

	def warning(self, msg):
		"""
		打印信息
		:param msg: 打印内容
		:return:
		"""
		self.logger.warning(str(msg))

	def error(self, msg):
		"""
		打印信息
		:param msg: 打印内容
		:return:
		"""
		self.logger.error(str(msg))


if __name__ == "__main__":
	log = Loger(journal=True)
	log.info(msg='1')
	log.error('2')
	log.debug('3')
	log.warning('4')
