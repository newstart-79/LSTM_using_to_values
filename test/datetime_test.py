"""
# author:gx
# data:2019/7/25-16:13 
# document:LSTM_using_to_values 
# name:test
# tool:PyCharm
# python version:3.7
"""
# datetime 时间序列包中的时间点的显示也应用
import pandas as pd
import numpy as np
import time
import os
from datetime import datetime
index = pd.date_range(start='2019-01-01',end='2019-06-30',freq='30min')  # 数据类型为datetimes的
print(index)
# print(type(index))
# str_index = index.strftime("%Y-%m-%d %H:%M")
# print(type(str_index))
data = pd.DataFrame(index=index,columns=['a b c d e f'.split(' ')])
print(data)
# print("年",data.index.year)
# print("月",data.index.month)
# print("日",data.index.day)
# print("小时",data.index.hour)
# print("分钟",data.index.minute)
# timestaps = pd.to_timestamp('2019-07-25')
# print(timestaps)
# # datastime = pd.to_datetime(df['ds'],unit='s') # unit=s 表示秒
