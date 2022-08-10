#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   DiskInformation.py
@Time    :   2022-08-10 11:10
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
import platform
from collections import namedtuple

# 获取磁盘信息
disk_ntuple = namedtuple('partition', 'device mountpoint fstype')
usage_ntuple = namedtuple('usage', 'total used free percent')

print(disk_ntuple)
print(usage_ntuple)