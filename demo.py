# -*- encoding: utf-8 -*-
"""
@File    :   demo.py
@Time    :   2022-10-24 22:45
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
from pltb import *

log = Loger()
log.info('demo')

service = ServiceManagement(service='docker.service', password='1')
service.status()

cmd = ComMand(password='1', cmd='apt update')
cmd.sudo()
