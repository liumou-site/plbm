# -*- encoding: utf-8 -*-
s = '''
@File    :   NetStatus.py
@Time    :   2022/04/13 11:19:25
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   liumou.site@qq.com
@Homepage : https://liumou.site
@Desc    :   网络管理
'''
from subprocess import getstatusoutput, getoutput
from os import path, system, getcwd
from sys import exit, platform
import socket
from requests import get


class NetworkTools:
	def __init__(self, ip=None, port=None):
		"""_summary_
        网络工具，用于判断网络是否正常
        Args:
            ip (str): 需要判断的IP
            port (int, optional): 需要判断的端口. Defaults to None.
        """
		self.ip = ip
		self.port = port
		self.status = False

	def pingstatus(self, server=None):
		"""_summary_
        使用ping检测网络连接
        Args:
            server (str, optional): 设置服务器地址. Defaults to self.ip.
        """
		self.status = False
		if server is None:
			server = self.ip
		print('正在检测： ', server)
		cmd = 'ping %s -c 5' % server
		if platform.lower() == 'win32':
			cmd = 'ping %s ' % server
		status = getstatusoutput(cmd)
		if status[0] == 0:
			print("Ping 连接成功: ", server)
			self.status = True
		else:
			print("Ping 连接失败: ", server)
		return self.status

	def httpstatus(self, server=None, port=None, url=None):
		"""_summary_
        检测HTTP服务是否正常访问,当设置URL的时候将会直接采用URL进行访问
        Args:
            server (str, optional): HTTP服务器地址. Defaults to self.ip.
            port (int, optional): 服务器端口. Defaults to self.port.
            url (str, optional): 完整URL. Defaults to None.
        Returns:
            bool: 是否访问成功
        """
		self.status = False
		if server is None:
			server = self.ip
		if port is None:
			port = self.port
		if url is None:
			url = str(server) + ":" + str(port)
		status = get(url=url)
		if status.status_code == 200:
			self.status = True
		if self.status:
			print("访问成功: ", url)
		else:
			print("访问失败: ", url)
		return self.status

	def downloadfile(self, url, filename=None, cover=False, md5=None):
		"""_summary_
        下载文件
        Args:
            url (str): 下载链接
            filename (str): 保存文件名,默认当前目录下以URL最后一组作为文件名保存
            cover (bool, optional): 是否覆盖已有文件. Defaults to False.
            md5 (str): 检查下载文件MD5值
        """
		if filename is None:
			filename = str(url).split("/")[-1]
			filename = path.join(getcwd(), filename)
		filename = path.abspath(filename)
		if path.exists(filename):
			if not cover:
				print("检测到已存在路径: ", filename)
				print("放弃下载： ", url)
				return True
			print("检测到已存在路径,正在删除...")
			c = 'rm -rf ' + filename
			if getstatusoutput(c)[0] == 0:
				print("删除成功: ", filename)
			else:
				print("删除失败,跳过下载")
				return False
		c = str("wget -c -O %s %s; echo $? > status" % (filename, url))
		system(c)
		if str(getoutput('cat status')) == '0':
			print("下载成功: ", filename)
			if md5:
				return True
		print("下载失败: ", filename)
		print("下载链接: ", url)
		print("保存路径: ", filename)
		return False


if __name__ == "__main__":
	up = NetworkTools()
	up.httpstatus(url='http://baidu.com')
	up.pingstatus(server='baidu.com')
