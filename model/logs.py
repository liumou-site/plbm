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


def logger_init(logger, file):
	"""
	初始化日志
	:param logger: 日志实例
	:param file: 记录文件
	:return:
	"""
	logger.setLevel('DEBUG')
	BASIC_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"
	DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
	formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
	chlr = logging.StreamHandler()  # 输出到控制台的handler
	chlr.setFormatter(formatter)
	chlr.setLevel('DEBUG')  # 也可以不设置，不设置就默认用logger的level
	fhlr = logging.FileHandler(file)  # 输出到文件的handler
	fhlr.setFormatter(formatter)
	logger.addHandler(chlr)
	logger.addHandler(fhlr)
