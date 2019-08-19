"""
# author:gx
# data:2019/7/26-14:53 
# document:LSTM_using_to_values 
# name:image_tanh_test
# tool:PyCharm
# python version:3.7
"""

# 功能：对tanh函数进行和图片的绘制，明确该函数是固定的图片形式
# 数据形式：y范围【-1，1】，x范围负无穷到正无穷

import matplotlib.pyplot as plt
import numpy as np

#函数
g =lambda z:(np.exp(z)-np.exp(-z))/(np.exp(z)+np.exp(-z))

start=-10 #输入需要绘制的起始值（从左到右）
start1 = -3
stop=10 #输入需要绘制的终点值
stop1 = 3
step=0.01#输入步长
num=(stop-start)/step #计算点的个数
x = np.linspace(start,stop,num)
y = g(x)
print(x,y)
num1 = (stop1-start1)/0.1
x1 = np.linspace(start1,stop1,num1)
y1 = g(x1)
print(x1,y1)

plt.figure()
plt.plot(x, y, label='tanh(-10,10)')
plt.plot(x1, y1, label='tanh(-5,5)')
plt.grid(True)#显示网格

plt.legend()#显示旁注
plt.show()
plt.close()