#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd

data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv" #填写url读取
df = pd.read_csv(data_url)