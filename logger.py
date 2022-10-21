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
import logging
from base import home_dir
from os import path


class Loger:
	def __init__(self, file=None,
	             console=True,
	             journal=False,
	             basic_level='DEBUG',
	             console_level='DEBUG',
	             journal_level='INFO',
	             basic_format="%(asctime)s:%(levelname)s:%(message)s",
	             date_format='%Y-%m-%d %H:%M:%S'):
		"""
		初始化日志模块
		:param file: 设置日志文件
		:param console: 是否在控制台显示信息(默认显示)
		:param journal: 是否记录日志到文件
		:param basic_level: 基本等级
		:param console_level: 控制台最低显示级别
		:param journal_level: 日志记录最低级别
		:param basic_format: 基本格式
		:param date_format: 时间格式
		"""
		self.basic_level = basic_level
		self.journal_level = journal_level
		self.console_level = console_level
		self.journal = journal
		self.console = console
		if file is None:
			file = path.join(home_dir, 'LiuMouLogs.log')
		self.file = file
		self.logger = logging.getLogger()

		self.basic_format = basic_format
		self.date_format = date_format
		self.logger.setLevel(self.basic_level)
		self.formatter = logging.Formatter(self.basic_format, self.date_format)
		if self.console:
			self.config_console()
		if self.journal:
			self.config_txt()

	def config_console(self):
		"""
		配置控制台终端信息
		:return:
		"""
		chlr = logging.StreamHandler()  # 输出到控制台的handler
		chlr.setFormatter(self.formatter)
		chlr.setLevel(self.console_level)  # 也可以不设置，不设置就默认用logger的level
		self.logger.addHandler(chlr)

	def config_txt(self):
		"""
		初始化日志
		:param logger: 日志实例
		:param file: 记录文件
		:return:
		"""
		fhlr = logging.FileHandler(self.file)  # 输出到文件的handler
		fhlr.setFormatter(self.formatter)
		self.logger.addHandler(fhlr)
