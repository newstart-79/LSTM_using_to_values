"""
# author:gx
# data:2019/7/30-10:10 
# document:LSTM_using_to_values 
# name:one_test
# tool:PyCharm
# python version:3.7
"""

# 对实际数据中的表现形式进行，测试代码
# test demo
import tensorflow as tf
import numpy as np
import pandas as pd

from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

class data_config():

    name = ['code', 'times', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    path = '../data/test.tsv'

def get_code_list(data):
    # data is Serise
    return set(data.values.tolist())



def get_data(config):
    data = pd.read_csv(config.path, names=config.name)
    get_code_list = set(data['code'].values.tolist())
    for code in get_code_list:
        data_code = data[data['code'] == code]
        time_list = []
        open_list = []
        high_list = []
        low_list = []
        close_list = []
        time_list.append([idx.split(',')[:16] for idx in data_code['times'].values])
        open_list.append([idx.split(',') for idx in data_code['2'].values])
        high_list.append([idx.split(',') for idx in data_code['3'].values])
        low_list.append([idx.split(',') for idx in data_code['4'].values])
        close_list.append([idx.split(',') for idx in data_code['5'].values])
        # time_list.append([idx.split(',')[:16] for idx in data.iloc[:, 1].values])
        # open_list.append([idx.split(',') for idx in data.iloc[:, 3].values])
        # high_list.append([idx.split(',') for idx in data.iloc[:, 4].values])
        # low_list.append([idx.split(',') for idx in data.iloc[:, 5].values])
        # close_list.append([idx.split(',') for idx in data.iloc[:, 6].values])

        time_list = np.array(time_list).flatten()
        open_list = np.array(open_list).flatten().astype('float')
        high_list = np.array(high_list).flatten().astype('float')
        low_list = np.array(low_list).flatten().astype('float')
        close_list = np.array(close_list).flatten().astype('float')
        # print(len(time_list),len(open_list),len(high_list),len(low_list),len(close_list))

        df = pd.DataFrame({'times': time_list, 'open': open_list, 'high': high_list, 'low': low_list, 'close': close_list})
        df.index = pd.to_datetime(df['times'],format="%Y-%m-%d")
        df = df.drop(['times'],axis=1)
        df.to_csv('../data/{}.csv'.format(code))
        # return df
def oper_arima(data):
    # 将时间序列数据分解：长期时间趋势，季节性时间趋势，周期性时间趋势，剩余的残差项
    # 查分得到一个相对平稳的时间序列值，一般情况下，差分2~3次，不可以再多了，否则丢失的细节太多
    # ARIMA 模型需要明确三个参数：p，d，q，ARIMA(p,d,q)模型，
    # p计算，AR
    # d计算，是差分的阶数，用来得到平稳序列。
    # q计算
    pass
def draw_data(x,y):
    plt.figure(figsize=(20, 10))
    plt.plot(x, y)
    plt.show()
from statsmodels.tsa.seasonal import seasonal_decompose

decomposition = seasonal_decompose(self.ts, freq=freq, two_sided=False)
# self.ts:时间序列，series类型;
# freq:周期，这里为1440分钟，即一天;
# two_sided:观察下图2、4行图，左边空了一段，如果设为True，则会出现左右两边都空出来的情况，False保证序列在最后的时间也有数据，方便预测。

self.trend = decomposition.trend
self.seasonal = decomposition.seasonal
self.residual = decomposition.resid
decomposition.plot()
plt.show()

if __name__ == '__main__':
    data = pd.read_csv('../data/000001.SZ.csv')
    # print(data.head(100))
    x = data['times'].values
    y = data['open'].values
    data_diff = data['open'].diff()
    draw_data(data_diff.index,data_diff.values)