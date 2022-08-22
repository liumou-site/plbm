# -*- encoding: utf-8 -*-
"""
@File    :   7z.py
@Time    :   2022-08-22 11:12
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   7z文件解压缩管理
"""
from py7zr import SevenZipFile
from os import listdir, path
import multiprocessing
from loguru import logger as echo


class Zip:
	def __init__(self, dir_path, processes):
		"""
		初始化参数
		:param dir_path: 需要解压缩的文件所在目录
		:param processes: 设置进程数量
		"""
		self.processes = processes
		if self.processes > multiprocessing.cpu_count():
			self.processes = multiprocessing.cpu_count()
			echo.warning(f"当前设置进程数量大于CPU内核数,已调整为: {self.processes}")
		self.dir_path = dir_path
		self.dir_list = []
		self.ok = []
		self.fail = []
		self.skip = []

	def info(self):
		echo.info(f"成功数量: {len(self.ok)}")
		echo.info(f"失败数量: {len(self.fail)}")
		echo.info(f"跳过数量: {len(self.skip)}")

	def zip(self, filename, sub):
		"""
		压缩文件夹
		:param filename: 生成的压缩文件名称(路径)
		:param sub: 需要压缩的文件夹
		:return:
		"""
		try:
			echo.info(f"压缩目录: {sub}")
			echo.info(f"生成文件: {filename}")
			z = SevenZipFile(file=filename, mode='w')
			z.writeall(sub)
			z.close()
			echo.info(f"压缩成功: {filename}")
			self.ok.append(filename)
		except Exception as e:
			echo.error(e)
			self.fail.append(filename)

	def unzip(self, filename, dest=None, password=None):
		"""
		解压7z文件
		:param password: 解压密码(如果有请传入)
		:param filename: 需要解压的文件
		:param dest: 解压目录,默认压缩文件所在目录
		:return:
		"""
		file_format = str(filename).split('.')[-1]
		if str(file_format).lower() == '7z'.lower():
			echo.debug("文件格式正确")
		else:
			echo.warning(f"文件格式不正确,跳过解压: {filename}")
			self.skip.append(filename)
			return False
		status = False
		if dest is None:
			dest = path.dirname(filename)
		echo.debug(f"正在解压: {filename}")
		echo.debug(f"解压目录： {dest}")
		if password:
			echo.debug(f"解压密码: {password}")
		try:
			if password is None:
				uz = SevenZipFile(file=filename, mode='r')
				uz.extractall(dest)
			else:
				uz = SevenZipFile(file=filename, mode='r', password=password)
				uz.extractall(dest)
			status = True
		except Exception as e:
			print(e)
		return status

	def start(self, unzip=False):
		"""
		开始
		:param unzip: 是否使用解压模式
		:return:
		"""
		dir_list = listdir(self.dir_path)
		cpu_ = multiprocessing.cpu_count()
		processes = len(dir_list)
		if len(dir_list) > cpu_:
			processes = cpu_
		echo.info(f"当前设置进程数: {processes}")
		pool = multiprocessing.Pool(processes=int(processes))
		if unzip:
			echo.info("进入解压模式")
			for file in dir_list:
				if path.isfile(file):
					file_path = path.join(self.dir_path, file)
					echo.info(f"正在解压: {file_path}")
					try:
						pool.apply_async(self.unzip, args=file_path)
					except Exception as e:
						echo.error(e)
				else:
					echo.debug(f"非文件，已跳过: {file}")
		else:
			for i in dir_list:
				zip_dir = path.join(self.dir_path, i)
				if path.isdir(zip_dir):
					file = f"{i}.7z"
					file = path.join(self.dir_path, file)
					if path.isfile(file) or str(file) == "git.7z":
						echo.info("已存在: %s" % file)
					else:
						echo.info(f"正在压缩： {file}")
						try:
							pool.apply_async(self.zip, (file, zip_dir))
						except Exception as e:
							echo.error(e)
		pool.close()
		pool.join()
		echo.info("结束!")
		self.info()


if __name__ == "__main__":
	cpu_ = multiprocessing.cpu_count()
	arg = ArgumentParser(description='当前脚本版本: 1.0', prog="7z文件解压缩-多线程版")
	arg.add_argument('-d', '--dir', type=str,
	                 help='设置需要解压缩的文件夹路径', required=True)
	arg.add_argument('-p', '--passwd', type=str,
	                 help='设置解压密码, 默认：无', required=False)
	arg.add_argument('-l', '--log', type=str, default=pwd,
	                 help='设置日志记录文件夹路径, 默认: %s' % pwd,
	                 required=False)
	arg.add_argument('-c', '--cpu', type=int, default=cpu_,
	                 help='设置进程数量,默认全核心: %s' % cpu_,
	                 required=False)
	arg.add_argument('-u', '--unzip', type=int, default=0,
	                 help='设置工作模式: 0(解压), 1(压缩), 默认: 1',
	                 required=False)
	args = arg.parse_args()
	dir_ = args.dir
	passwd_ = args.password
	un_ = args.unzip
	c_ = args.cpu
	u_ = False
	if int(un_) == 0:
		u_ = True
	u = Zip(dir_path=dir_, processes=int(c_))
	u.start(unzip=u_)
