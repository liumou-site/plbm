#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   DiskInformation.py
@Time    :   2022-08-10 11:10
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
import psutil

for i in psutil.disk_partitions(all=False):
	dev = i.device
	print(f"设备: {dev}")
	info = psutil.disk_usage(str(dev))
	print(f"总容量: {info.total / 1024 /1024} MB")
	print(f"使用量: {info.used / 1024 /1024} MB")
	print(f"剩余量: {info.free / 1024 /1024} MB")
