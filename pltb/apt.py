# -*- encoding: utf-8 -*-
"""
@File    :   apt.py
@Time    :   2022-09-05 09:17
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
from pltb.cmd import ComMand


class AptManagement:
	def __init__(self, password, log=False, terminal=False):
		"""
		Apt 管理
		:param password: 主机密码
		:param log: 是否启用日志
		:param terminal: 是否使用终端执行命令(针对个别Linux发行部才起作用)
		"""
		self.terminal = terminal
		self.log = log
		self.password = password
		self.cmd = ComMand(password=self.password, cmd='which apt', terminal=self.terminal, logs=self.log)

	def install(self, pac='git', update=False):
		"""
		安装在线包
		:param update: 是否更新源索引(默认不会更新源索引)
		:param pac: 需要安装的包(字符串)
		:return:
		"""
		if update:
			self.update()
		print("Installing %s ..." % pac)
		cmd = str("apt install -y %s" % pac)
		return self.cmd.sudo(cmd=cmd, name='Install %s' % pac)

	def update(self):
		"""

		:return:
		"""
		return self.cmd.sudo(cmd="apt update", name="Update Sources")

	def local_install_f(self, file):
		"""
		实现apt install -y -f ./install.deb的效果
		:param file:
		:return:
		"""
		return self.cmd.sudo(cmd="apt install -y -f %s" % file, name='Install Local Package')

	def install_f(self):
		"""
		执行apt install -y -f 修正环境,此功能慎用,如果处理不好可能对系统组件造成损害
		:return:
		"""
		self.update()
		return self.cmd.sudo(cmd="apt install -y -f", name='Install Local Package')

	def reinstall_rc(self, update=False):
		"""
		一键修复 rc 状态的包列表
		:param update: 是否更新源索引(默认不会更新源索引)
		:return:执行结果(bool)
		"""
		if update:
			self.update()
		cmd = "apt install -y --reinstall `dpkg -l | grep -v ii  | grep rc | awk '{print $2}' | sed '1,5 d'`"
		return self.cmd.sudo(cmd=cmd, name='List of packages to repair rc status', terminal=False)

	def remove_rc(self, update=False):
		"""
		一键卸载 rc 状态的包列表
		:param update: 是否更新源索引(默认不会更新源索引)
		:return:执行结果(bool)
		"""
		if update:
			self.update()
		cmd = "apt purge -y `dpkg -l | grep -v ii  | grep rc | awk '{print $2}' | sed '1,5 d'`"
		return self.cmd.sudo(cmd=cmd, name='List of packages in unloaded rc status', terminal=False)

	def upgrade(self, update=True):
		"""
		执行apt-get upgrade时，upgrade是根据update更新的索引记录来下载并更新软件包
		:param update: 是否更新源索引(默认不会更新源索引)
		:return:
		"""
		if update:
			self.update()
		cmd = 'apt upgrade -y --fix-missing'
		return self.cmd.sudo(cmd=cmd, terminal=False, name='更新系统-upgrade')

	def upgrade_dist(self, update=True):
		"""
		执行apt-get dist-upgrade时，除了拥有upgrade的全部功能外，dist-upgrade会比upgrade更智能地处理需要更新的软件包的依赖关系
		:param update: 是否更新源索引(默认不会更新源索引)
		:return: 更新结果
		"""
		if update:
			self.update()
		cmd = 'apt dist-upgrade -y --fix-missing'
		return self.cmd.sudo(cmd=cmd, terminal=False, name='更新系统-dist-upgrade')
