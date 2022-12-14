#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from os import path
from pltb.cmd import ComMand
from pltb.apt import AptManagement
from subprocess import getoutput
from pltb.logger import Loger


class Source:
	def __init__(self, passwd, debug=False, mirrors="mirrors.cloud.tencent.com"):
		self.mirrors = mirrors
		self.source = '/etc/apt/sources.list'
		self.source_bak = '/etc/apt/sources.list.bak'
		self.cmd = ComMand(password=passwd)
		self.resease = getoutput("cat /etc/os-release  | grep ^ID=").split("=")[1].lower()
		self.apt = AptManagement(password=passwd)

	def bak(self):
		if not path.isfile(self.source_bak) and path.isfile(self.source):
			self.cmd.sudo(cmd="cp -rf %s %s" % (self.source, self.source_bak), name='Bak Sources')

	def get(self):
		cmd = "cat /etc/apt/sources.list | grep ^deb | grep http | sed -n 1p"
		info = str(getoutput(cmd=cmd))
		if len(info) >= 5:
			try:
				url = str(info).split(" ")[1]
				http_ = str(url).split(":")[0]
				host_ = str(url).split("//")[1].split("/")[0]
				http_cmd = "sed -i 's@%s@https@g' %s" % (http_, self.source)
				# print(host_)
				host_cmd = "sed -i 's@%s@%s@g' %s" % (host_, self.mirrors, self.source)
				# print(host_cmd)
				self.cmd.sudo(cmd=http_cmd, name='Http')
				self.cmd.sudo(cmd=host_cmd, name='host')
			except Exception as e:
				logger.error(str(e))
		cmd = "cat /etc/apt/sources.list | grep ^deb | grep http | grep security | sed -n 1p"
		info = str(getoutput(cmd=cmd))
		if len(info) >= 5:
			try:
				url = str(info).split(" ")[1]
				http_ = str(url).split(":")[0]
				host_ = str(url).split("//")[1].split("/")[0]
				http_cmd = "sed -i 's@%s@https@g' %s" % (http_, self.source)
				host_cmd = "sed -i 's@%s@%s@g' %s" % (host_, self.mirrors, self.source)
				# print(http_)
				# print(http_cmd)
				# print(host_)
				# print(host_cmd)
				self.cmd.sudo(cmd=http_cmd, name='Http-security')
				self.cmd.sudo(cmd=host_cmd, name='host-security')
			except Exception as e:
				logger.error(str(e))

	def start(self):
		logger.error('ee')
		# self.bak()
		# self.get()
		# self.apt.update()


if __name__ == "__main__":
	p = Loger()
	logger = p.logger
	logger.info("sad")
	s = Source(passwd='1', debug=True)
	s.start()
