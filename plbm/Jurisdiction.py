#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Jurisdiction.py
@Time    :   2022/04/25 16:54:45
@Author  :   村长
@Version :   1.0
@Contact :   liumou.site@qq.com
@Desc    :   权限验证模块
'''

from os import system
from subprocess import getstatusoutput, getoutput
from sys import exit, platform
from plbm.logger import Loger
from plbm.base import os_arch, os_ver, os_type, username, uid


class Jurisdiction:
    def __init__(self, passwd, logs=True, log_file=None):
        """_summary_
        判断权限是否正确
        Args:
            passwd (str): 设置主机密码
        """
        self.log_file = log_file
        self.logs = logs
        if platform.lower() == 'win32':
            print("不支持Windows系统")
            exit(2)
        self.passwd = passwd
        self.super_permissions = False
        self.os_ver = os_ver
        self.arch = os_arch
        self.os_type = os_type
        log = Loger(file=self.log_file)
        self.loggers = log.logger

    def verification(self, name):
        """_summary_
        检测sudo权限是否能够获取并设置正确的密码
        最终密码可以通过实例变量获取(self.passwd)
        Args:
            name (str): 调用的函数名称
        Returns:
            bool: 是否取得sudo权限
        """
        if str(username).lower() == 'root' or int(uid) == 0:
            if self.logs:
                self.loggers.info('已处于root权限')
            return True
        if self.os_type.lower() == 'uos'.lower():
            self.developer()
        else:
            self.super_permissions = True
        if self.super_permissions:
            s = True
            err = 0
            while s:
                self.loggers.info("当前密码：%s" % self.passwd)
                self.loggers.info('调用函数: %s' % name)
                c = "echo %s | sudo -S touch /d" % self.passwd
                d = "echo %s | sudo -S rm -f /d" % self.passwd
                print(c)
                res = system(c)
                if str(res) == '0':
                    system(d)
                    return True
                else:
                    self.passwd = input('请重新输入密码:\n')
                    err += 1
                if int(err) >= 3:
                    print('密码输入错误数量达到限制,将使用非特权模式检查,部分信息或功能将无法使用')
                    return False

    def developer(self):
        """_summary_
        检查是否开启开发者模式
        Returns:
            bool: 是否开启开发者
        """
        dev_file = "/var/lib/deepin/developer-install_modes/enabled"
        dev1 = str(getoutput(cmd="cat %s") % dev_file).replace(" ", '').replace('\n', '')

        dev_file2 = "/var/lib/deepin/developer-install_mode/enabled"
        dev2 = str(getoutput(cmd="cat %s") % dev_file2).replace(" ", '').replace('\n', '')

        dev_file3 = "cat /var/lib/deepin/developer-mode/enabled"
        dev3 = str(getoutput(cmd=dev_file3)).replace(" ", '').replace('\n', '')

        terminal_mode = False
        if dev1 == "1" or dev2 == "1" or dev3 == "1":
            terminal_mode = True
        elif str(getoutput('echo $UID')) != '0' and str(getoutput('echo $USER')) == "root" or str(getoutput('echo $UID')) == '0':
            terminal_mode = True
        self.super_permissions = terminal_mode
        if self.super_permissions:
            print('已开启开发者')
            return True
        else:
            print('开发者未开启')
        return False
    
    def sudo(self, cmd, display=True):
        """
        执行sudo命令
        Args:
            cmd (str): 需要执行的命令
            display (bool, optional): _description_. Defaults to True.
        """
        c = str("echo % s | sudo -S %s" % (self.passwd, cmd))
        status = '1'
        info = ''
        if display:
            c = str("echo % s | sudo -S %s;echo $? > status" % (self.passwd, cmd))
            system(c)
            status = getoutput('cat status')
        else:
            get = getstatusoutput(c)
            status = get[1]
            info = get[0]
        if str(status) == '0':
            return True
        return False
