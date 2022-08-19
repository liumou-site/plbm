#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   usage.py
@Time    :   2022-08-11 11:55
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   CPU管理
"""
import psutil


class CpuManger:
	def __init__(self):
		self.pid_list = psutil.pids()
	
	def usage_pid(self, pid=None):
		"""
		获取PID的占用情况
		:param pid:
		:return:
		"""
		p = psutil.Process(pid=pid)
		# 获取进程启动命令
		command = p.cmdline()
		print(p.name())
		print(p.cpu_times())
		print(p.cpu_percent())
		print(p.cpu_affinity())
		print(p.cpu_num())
		print(p.memory_info())
		print(p.memory_percent())
		g = psutil.cpu_percent()
		print(g)

if __name__ == "__main__":
	up = CpuManger()
	up.usage_pid(pid=58493)
