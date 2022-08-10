#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   f.py
@Time    :   2022-08-10 17:59
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
from os import walk, path

for dir_path,dir_name,file_name in walk("d:\\"):
	for filename in file_name:
		print(path.join(dir_path, filename))