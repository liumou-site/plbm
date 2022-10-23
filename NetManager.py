# -*- encoding: utf-8 -*-
s = '''
@File    :   NetManager.py
@Time    :   2022/04/17 01:06:40
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   liumou.site@qq.com
@Homepage : https://liumou.site
@Desc    :   网络管理模块
'''
print(s)
from subprocess import getoutput
from cmd import ComMand


class NetManager(object):
	def __init__(self, password=None, ipv4=None, gateway=None,  netmask=24, dns1=None, dns2=None, subnet=None, device=None, log=True):
		"""
		网络管理模块,参数均为可选传参，请根据实际需求传入
		:param password: (str, optional): 设置主机密码. Defaults to None.
		:param ipv4: (str, optional): 设置IP地址. Defaults to "192.168.1.138".
		:param gateway: (str, optional): 设置网关. Defaults to "192.168.1.1".
		:param netmask: (int, optional): 设置子网掩码. Defaults to 24.
		:param dns1: (str, optional): 设置DNS1. Defaults to "114.114.114.114".
		:param dns2: (str, optional): 设置DNS2. Defaults to "119.29.29.29".
		:param subnet: (str, optional): 设置网段,一般是自动尝试配置IP需要. Defaults to '192.168.1.'.
		:param device: (str, optional): 设置网卡名称. Defaults to 'ens33'.
		:param log: (bool, optional): 是否启用日志功能
		"""
		if ipv4 is None:
			ipv4 = "192.168.1.138"
		self.ipv4 = ipv4
		#
		if gateway is None:
			gateway = "192.168.1.1"
		if dns1 is None:
			dns1 = "114.114.114.114"
		if dns2 is None:
			dns2 = "119.29.29.29"
		if subnet is None:
			subnet = "192.168.1."
		if device is None:
			device = 'ens33'
		self.log = log
		# 主机密码
		self.password = password
		# 网段
		self.subnet = subnet
		# IP地址
		self.ipv4 = ipv4
		# 网关
		self.gateway = gateway
		# DNS1
		self.dns1 = dns1
		# DNS2
		self.dns2 = dns2
		# 子网掩码
		self.netmask = netmask
		# 连接名称
		self.connect_name = 'Y'
		# 连接模式
		self.connect_mode = 'auto'
		# 连接列表
		self.connect_list = []
		# DNS列表
		self.dns_list = []
		# 网卡设备
		self.device = device
		self.cmd = ComMand(password=password)

	def connect_create(self, name="Y", mode='auto'):
		"""_summary_
        创建连接
        Args:
            name (str, optional): 连接名称. Defaults to "Y".
        """
		pass

	def cmd_status(self, cmd):
		"""
        执行
        """

	pass

	def connect_delete(self, name=None):
		"""_summary_
        删除连接
        Args:
            name (str, optional): _description_. Defaults to "Y".
        """
		if name is None:
			name = self.connect_name
		if self.get_connect_list() and name in self.connect_list:
			c = str("""nmcli connection  delete %s""" % name)
			print("正在删除链接: ", name)

	def get_device_list(self):
		"""_summary_
        获取设备列表
        """
		pass

	def get_connect_list(self):
		"""
        获取连接列表
        """
		c = """nmcli con  | grep -v UUID | awk '{print $1}'"""
		self.connect_list = getoutput(c).split("\n")
		if len(self.connect_list) == 0:
			print("检测不到列表列表")
			return False
		return True

	def get_current(self):
		"""
        获取当前配置,包含: IP4、网关、掩码
        """
		pass

	def get_dns(self):
		"""
        获取DNS配置列表
        """
		pass
