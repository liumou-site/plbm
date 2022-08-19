#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   iptables.py
@Time    :   2022-08-11 11:55
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   防火墙管理
"""

from sys import exit
from subprocess import getstatusoutput, getoutput
from os import system, getenv, getcwd, path
from datetime import datetime


class IpTables:
	def __init__(self, bak_path=getcwd()):
		"""
		设置类变量
		:param bak_path: 设置规则备份路径
		"""
		self.bak_path = bak_path
		self.agreement = 'TCP'
		self.port = 80
		self.source = "0.0.0.0/0"
		self.zone = 'public'
		self.ok = False
		# 设置方向，默认: 进口
		self.direction = "INPUT"
		# 记录已配置的端口列表
		self.port_list = []
		# 记录端口详细情况
		self.port_dic = {}
		# 查看已配置且接受的端口列表
		self.port_accept_list = []
		# 记录ID和端口的关系
		self.port_id_port = {}
		# 设置系统服务名称
		self.service = 'ipsec'
		self.env()
		# 备份配置
		self.backups()
	
	def env(self):
		"""
		环境检测
		:return:
		"""
		if getenv(key="USER").lower() == 'root'.lower():
			print("当前使用的是超级用户")
		else:
			print("当前使用的不是超级用户，可能无法配置成功,请切换用户或者使用sudo执行")
			exit(1)
	
	def add_port_appoint_ip(self):
		"""
		添加特定IP接受或拒绝访问特定端口
		:return:
		"""
		pass
	
	def save(self, name):
		"""
		保存更改
		"""
		save_ = getstatusoutput('iptables-save')
		if save_[0] == 0:
			print(f"[ {name} ] Saved successfully")
		else:
			print(f"[ {name} ] Saved successfully")
			print(save_[1])
	
	def set_port_appoint_source(self, agreement=None, port=None, source=None, ACCEPT=True):
		"""
		设置特定IP接受或拒绝访问特定端口
		:param agreement: 协议(tcp/udp/icmp)
		:param port: 端口号
		:param source: 设置源地址
		:param ACCEPT: 是否接受数据
		:return: 配置结果(bool)
		"""
		mode = "ACCEPT"
		if ACCEPT:
			mode = "REJECT"
		if agreement is None:
			agreement = self.agreement
		if port is None:
			port = self.port
		if source is None:
			source = self.source
		cmd = f"iptables -A INPUT -p {agreement} -s {source} --dport {port} -j {mode}"
		print(cmd)
	
	def open_port_all_ip(self, agreement=None, port=None):
		"""
		开放端口给所有IP
		:param agreement: 协议(tcp/udp),默认:TCP
		:param port: 端口号,默认: 80
		:return: 配置结果
		"""
		if agreement is None:
			agreement = self.agreement
		if port is None:
			port = self.port
		cmd = f"iptables -A INPUT -p {agreement} --dport {port} -j ACCEPT "
		print(cmd)
		c = getstatusoutput(cmd)
		if c[0] == 0:
			print("Successful opening: ", port)
			self.save(name=f"open port {port}")
			return True
		else:
			print("Successful failed: ", port)
		return False
	
	def delete_port(self, port):
		"""_summary_
		通过端口删除策略
		Args:
		port (int): 需要删除的端口
		"""
		self.get()
		del_id_list = []
		# print(f"port_id_port: {self.port_id_port}")
		for id_ in self.port_id_port:
			port_ = self.port_id_port[id_]
			# print(f"port_: {port_}")
			# print(f"port: {port}")
			if int(port_) == int(port):
				del_id_list.append(id_)
		# print(f"del_id_list: {del_id_list}")
		if del_id_list:
			self.delete_port_to_id(id=del_id_list, auto=True)
	
	def delete_port_to_id(self, id=None, auto=False):
		"""
		通过ID删除策略
		:param id: 需要删除的端口id列表
		:param auto: 是否使用自动模式
		:return:
		"""
		if id is None:
			id = []
		if not auto:
			print("使用对答模式")
			print(getstatusoutput("iptables -L -n --line-numbe")[1])
			id_ = input("请输入需要删除的策略ID值(整数),每个ID之间使用空格间隔\n")
			id = str(id_).split(' ')
		del_sum = 0
		for id_del in id:
			print("\nDelete source ID: ", id_del)
			if int(del_sum) != 0:
				print(f"由于条目发生变化, 源规则ID [ {id_del} ] 减去 [ {del_sum} ]")
			id_del = int(id_del) - int(del_sum)
			info = f"iptables -L -n --line-number | grep ^{id_del}"
			cmd = f"iptables -D INPUT {id_del}"
			de = getstatusoutput(cmd)
			if de[0] == 0:
				print('Delete succeeded: ', id_del)
			else:
				print("Delete succeeded: ", id_del)
				print(getoutput(info))
			del_sum += 1
	
	def print_all(self):
		"""
		打印全部已配置策略的端口
		:return:
		"""
		print("当前系统已配置的端口列表如下")
		for port in self.port_list:
			print(port)
	
	def get(self):
		"""
		获取已经开放的端口
		:return:
		"""
		cmd = "iptables -L -n --line-number | grep -v ^Chain | grep -v ^num | sed 's/\t/_/g'"
		g = getstatusoutput(cmd)
		if g[0] == 0:
			# print("执行查询成功")
			port_str_list = str(g[1]).split('\n')
			for port_str in port_str_list:
				port_str_list = str(port_str).replace(' ', '_').split('_')
				result = []
				if len(port_str_list) >= 2:
					for i in port_str_list:
						if str(i) != '':
							result.append(i)
					# print(f"result: {result}")
					port_ = str(result[7]).split(':')[1]
					# 记录ID与端口的dic
					self.port_id_port[result[0]] = port_
					if port_ not in self.port_list:
						self.port_dic[port_] = result
						self.port_list.append(port_)
						if result[1] == 'ACCEPT':
							self.port_accept_list.append(port_)
		else:
			print("执行查询失败")
	
	def start(self):
		"""
		启动服务
		:return:
		"""
		cmd = "systemctl restart %s" % self.service
		c = getstatusoutput(cmd)
		if c[0] == 0:
			self.status()
		else:
			print("%s service startup failed" % self.service)
			print(c[1])
			exit(1)
	
	def status(self):
		"""
		获取当前状态
		:return:
		"""
		service_get = getstatusoutput(
			cmd='systemctl -all | grep iptables.service')
		if service_get[0] == 0:
			if service_get[1]:
				self.service = 'iptables.service'
		status_cmd = """systemctl status  %s | grep Ac | awk '{print $2}'""" % self.service
		cmd = getstatusoutput(status_cmd)
		if cmd[0] == 0:
			if str(cmd[1]).lower() == 'active'.lower():
				print("Service started")
				self.ok = True
				return True
			else:
				self.start()
		else:
			print("Service status query failed")
			print(cmd[1])
			exit(2)
	
	def backups(self):
		"""
		备份源规则
		:return: 备份结果
		"""
		time_ = datetime.now()
		time_ = str(time_).replace('-', '_').replace(":", '_').replace(' ', '').split('.')[0]
		time_ = str(time_) + ".ini"
		filename = path.join(self.bak_path, time_)
		cmd = f"iptables-save > {filename}"
		print(f"Set up backup files: {filename}")
		if getstatusoutput(cmd)[0] == 0:
			print('Current policy backup succeeded')
			return True
		else:
			print('Current policy backup Failed')
			return False
	
	def clean_all(self):
		"""
		删除所有规则
		:return:
		"""
		self.backups()
		sum = 0
		for cmd in ["iptables -X", "iptables -F", "iptables -Z"]:
			if getstatusoutput(cmd)[0] == 0:
				sum += 1
		if int(sum) == 3:
			print("Cleared successfully")
		else:
			print("Cleanup failed")


if __name__ == "__main__":
	up = IpTables()
	up.get()
	up.status()
	up.open_port_all_ip(port=8081)
	up.print_all()
	up.delete_port(port=8081)
	up.clean_all()
