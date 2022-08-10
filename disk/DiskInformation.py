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


class DiskInfo:
	def __init__(self):
		self.dev_list = []
		self.partition_path = {}
		self.Partition_total = {}
		self.Partition_used = {}
		self.Partition_free = {}

	def base(self):
		"""
		获取基础信息
		:return:
		"""
		# 获取设备(分区)列表
		for i in psutil.disk_partitions(all=False):
			dev = i.device
			self.dev_list.append(dev)
			# 记录设备与挂载路径信息
			self.partition_path[dev] = i.mountpoint
			# 获取设备使用情况
			info = psutil.disk_usage(self.partition_path[dev])
			# 记录设备与总容量
			self.Partition_total[dev] = info.total
			# 记录设备与使用量
			self.Partition_used[dev] = info.used
			# 记录设备与剩余量
			self.Partition_free[dev] = info.free

	def info(self):
		"""
		获取磁盘使用情况
		:return:
		"""
		self.base()
		for dev in self.dev_list:
			print('\n')
			print(f"当前设备/分区: {dev}")
			print(f"挂载路径: {self.partition_path[dev]}")
			print(f"总容量: {self.Partition_total[dev] / 1000 / 1000} MB")
			print(f"使用量: {self.Partition_used[dev] / 1000 / 1000} MB")
			print(f"剩余量: {self.Partition_free[dev] / 1000 / 1000} MB")
			print(f"使用率: {str(float(self.Partition_used[dev]) / float(self.Partition_total[dev]) * 100)[0:4]} %")


if __name__ == "__main__":
	up = DiskInfo()
	up.info()
