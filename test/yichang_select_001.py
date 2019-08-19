"""
# author:gx
# data:2019/8/15-14:43 
# document:LSTM_using_to_values 
# name:yichang_select_001
# tool:PyCharm
# python version:3.7
"""
import pandas as pd
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
from scipy.optimize import leastsq # 最小二乘计算

def Fun(p, x):  # 定义拟合函数形式
    a1, a2, a3 = p
    return a1 * x ** 2 + a2 * x + a3


def error(p, x, y):  # 拟合残差
    return Fun(p, x) - y


def main(x,col):
    xx = np.arange(0,len(x),1)
    # x = np.linspace(-10, 10, 100)  # 创建时间序列
    p_value = [-2, 5, 10]  # 原始数据的参数
    noise = np.random.randn(len(xx))  # 创建随机噪声
    y = Fun(p_value, x) + noise * 2  # 加上噪声的序列
    p0 = [0.1, -0.01, 100]  # 拟合的初始参数设置
    para = leastsq(error, p0, args=(x, y))  # 进行拟合
    y_fitted = Fun(para[0], x)  # 画出拟合后的曲线

    plt.figure()
    plt.plot(x, y, 'r', label='Original curve')
    plt.plot(x, y_fitted, '-b', label='Fitted curve')
    plt.legend()
    plt.show()
    plt.savefig('../data/{}_fun.jpg'.format(col))
    print(para[0])
    # plt.close()

def data_get():
    pass
def draw_original(data,col):
    plt.figure(figsize=(12,6))
    plt.plot(data.index,data.values)
    plt.show()
    plt.savefig('../data/{}.jpg'.format(col))
    plt.close()
if __name__ == '__main__':
    # main()
    data = pd.read_pickle('../data/other.pkl').loc['2017-09-01':'2018-01-01']
    print(data.shape)
    # data = data.loc[:,:100]
    data = data.dropna(axis=1,how='all').iloc[:,0:30]
    data = data.fillna(method='bfill',axis=1)

    for col in data.columns:
        data_use = data[col[0],col[1],col[2]]
        if len(set(data_use.values))>= 3:
            main(data_use.values,col)
            # draw_original(data_use,col)
        # print(data_use.index)
        else:
            print(col)