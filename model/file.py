# -*- encoding: utf-8 -*-
s = '''
@File    :   file.py
@Time    :   2022/04/13 20:16:27
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   liumou.site@qq.com
@Homepage : https://liumou.site
@Desc    :   文件管理
'''
from subprocess import getstatusoutput, getoutput
from os import path, system
from sys import exit
import hashlib


class FileManager:
	def __init__(self, password=None, file=None):
		"""_summary_
        文件管理模块
        Args:
            password (str, optional): 设置主机密码. Defaults to None.
        """
		self.passwd = password
		self.md5 = None
		self.file = file
	
	def exists(self, paths):
		"""_summary_
        判断文件是否存在
        Args:
            paths (_type_): _description_
        """
		if path.exists(paths):
			return True
		return False
	
	def sudo(self, cmd, display=True):
		"""_summary_
        执行超级命令
        Args:
            cmd (str): 需要执行的命令
        """
		c = str("echo % s | sudo -S %s" % (self.passwd, cmd))
		if display:
			c = str("echo % s | sudo -S %s;echo $? > s" % (self.passwd, cmd))
			system(c)
			status = getoutput('cat s')
			if str(status) == '0':
				return True
			print(c)
			return False
		else:
			status = getstatusoutput(c)
			if status[0] == 0:
				return True
		print(c)
		return False
	
	def mkdir(self, paths, recursion=True, sudo=False, display=False):
		"""_summary_
        创建文件夹
        Args:
            paths (str): 需要创建的文件夹路径
            recursion (bool, optional): 是否创建递归路径. Defaults to True.
            sudo (bool, optional): 是否使用sudo权限. Defaults to False.
            display (bool, optional): 是否显示执行信息. Defaults to False.
        Returns:
            bool: 是否创建成功
        """
		status = False
		if path.isdir(paths):
			print('已存在路径: ', paths)
			return True
		c = str("mkdir -p %s" % paths) if recursion else str("mkdir %s" % paths)
		if sudo:
			status = self.sudo(cmd=c, display=display)
		else:
			status_ = getstatusoutput(c)
			if status_[0] == 0:
				status = True
			else:
				print(status_[1])
		return status
	
	def rmdir(self, path, sudo=False, display=False):
		"""_summary_
        删除文件夹
        Args:
            path (str): 需要删除的文件夹路径
            sudo (bool, optional): 是否使用sudo权限. Defaults to False.
            display (bool, optional): 是否显示执行信息. Defaults to False.
        Returns:
            bool: 是否创建成功
        """
		status = False
		if not path.isdir(path):
			print("路径不存在,无需删除: " + path)
			return True
		c = str("rm -rf " + path)
		if sudo:
			status = self.sudo(cmd=c, display=display)
		else:
			status_ = getstatusoutput(c)
			if status_[0] == 0:
				status = True
			else:
				print(status_[1])
		return status
	
	def getmd5(self, filename=None):
		"""
		获取文件MD5值
		:param filename: 需要获取MD5的文件,通过实例.md5获取值
		:return:
		"""
		if filename is None and self.file:
			filename = self.file
		m = hashlib.md5()  # 创建md5对象
		with open(filename, 'rb') as fobj:
			while True:
				data = fobj.read(4096)
				if not data:
					break
				m.update(data)  # 更新md5对象
		
		return m.hexdigest()  # 返回md5对象
