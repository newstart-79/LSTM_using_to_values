"""
# author:gx
# data:2019/8/16-13:51 
# document:LSTM_using_to_values 
# name:time_series
# tool:PyCharm
# python version:3.7
"""
# 时间序列，流程图
# 时间序列数据

import pandas as pd
import numpy as np
import datetime
import dtw
import statsmodels

# 短期环比SS： count(sum(nowvalues-1)>threshold)>count_num
#  threshold = min(max-avg,avg-min),求取规定窗口时间内的，最大值max，平均值avg和最小值min

# 长期环比LS:

def huanbi_ss(datas,count_num=7):
    max_d = np.max(datas)
    min_d = np.min(datas)
    avg_d = np.average(datas)

    # 动态阈值计算
    threshold = np.min(max_d-avg_d, avg_d-min_d)
    count = len(datas[datas > threshold])
    if count >= count_num:
        print('该段时间存在异常')
    else:
        print('处在正常范围内')
    return count

def huanbi_ls(datas):
    exp_average = datas.ewm(span=30, ignore_na=True, adjust=True).mean()
    exp_std = datas.ewm(span=30, ignore_na=True, adjust=True).std()
    # 使用3 - sigma理论来判断新的input是否超过了容忍范围
    # print(exp_std,exp_average)
    print(abs(datas.values[-1] - exp_average.values[-1]), 3 * exp_std.values[-1])
    if abs(datas.values[-1]-exp_average.values[-1]) > 3*exp_std.values[-1]:
        print('存在异常')
    else:
        print('区间内数据正常！')

def tongbi_chain(datas):
    pass

"""时间序列平滑处理"""
def diff_smooth(ts, interval):

    # 间隔为1小时
    wide = interval/60  # 时间间隔的宽度
    # 差分序列
    dif = ts.diff().dropna()
    # 描述性统计得到：min，25%，50%，75%，max值
    td = dif.describe()
    # 定义高点阈值，1.5倍四分位距之外
    high = td['75%'] + 1.5 * (td['75%'] - td['25%'])
    # 定义低点阈值
    low = td['25%'] - 1.5 * (td['75%'] - td['25%'])

    i = 0
    forbid_index = dif[(dif > high) | (dif < low)].index  # 超出标准部分的下标,时间序列列表
    while i < len(forbid_index) - 1:
        # 发现连续多少个点变化幅度过大
        n = 1
        # 异常点的起始索引
        start = forbid_index[i]
        if (i+n) < len(forbid_index)-1:
            while forbid_index[i+n] == start + datetime.timedelta(hours=n):
                n += 1
        i += n - 1  # (自加之前先-1)
        # 异常点的结束索引
        end = forbid_index[i]
        # 用前后值的中间值均匀填充
        value = np.linspace(ts[start - datetime.timedelta(hours=wide)], ts[end + datetime.timedelta(hours=wide)], n)
        ts[start: end] = value
        i += 1
    return ts

""" 数据切割求dtw"""
def datas_split(ts):
    # x，y表示前后的两个时间段的数据对比
    # 找到时间周期T
    ts_T = statsmodels.seasonal_decompose('')


    # 数据切割成，N/T 分

    T = 64
    dist, cost, acc, path = dtw(T, T+1, dist=lambda x, y: np.linalg.norm(x - y, ord=1))
    # dist 越大表示两个数据的差距越大，反之亦然。


if __name__ == '__main__':
    pass