"""
# author:gx
# data:2019/8/16-9:47 
# document:LSTM_using_to_values 
# name:screen_001
# tool:PyCharm
# python version:3.7
"""
# 功能：时间序列数据切分画图
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Config():
    data_source='../data/input' # 数据路径
    image_save_source = '../data/output/imagesave' # 图片保存路劲
    image_size = (12,8)
    data_length = 7*24


class draw_image(object):
    def __init__(self, config):
        self.data_source = config.data_source  # 数据
        self.image_save_source = config.image_save_source  # 保存 图片
        self.data_lenght = config.data_length  #切割数据长度
        # 图片的形状
        self.image_size = config.image_size  # 单张图片大小


    def data_split(self):
        data = pd.read_pickle(self.data_source)
        for i in range(0, len(data), self.data_lenght):
            data_cut = data[i:i + self.data_lenght]
            yield data_cut
            # 需要画图的数据

    def draw_plot(self,data,n,m):
        fig = plt.figure(figsize=(self.image_size[0]*n, self.image_size[1]*m))
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        count = 0
        for i in range(int(n*m)):
            count += 1
            ax = fig.add_subplot(n, m, count)  # 数量 n行，m列
            plt.plot(data.index, data.values)
            plt.scatter(data.index, data.values)
            plt.gcf().autofmt_xdate() # 自动调整


if __name__ == '__main__':
    image_x = int(input('请输入单张图片的长'))
    image_y = int(input("请输入单张图片的宽"))
    image_num = int(input('请输入图片的数量'))



