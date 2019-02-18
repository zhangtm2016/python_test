#!/usr/bin/python
# -*- coding: UTF-8 -*-

#利用税务数据分析美国人群收入情况

import csv
import pandas as pd
from io import StringIO
from urllib import request


url='https://commondatastorage.googleapis.com/ckannet-storage/2012-01-07T150817/data.csv'
s = request.urlopen(url).read().decode('utf8')  # 1 读取数据串

dfile = StringIO(s)      # 2 将字符串转换为 StringIO对象，使其具有文件属性
creader = csv.reader(dfile)  # 3 将流 转换为可迭代的 reader（csv row）
dlists=[rw for rw in creader]  # 4 其他转换、操作
