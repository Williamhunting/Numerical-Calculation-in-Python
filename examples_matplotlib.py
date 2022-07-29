# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:32:16 2021

@author: 28501
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 2*x + 1
z = x**2
plt.figure() #想要每个数据重新开一个图，就要重新写一个plt.figure(),否则所有数据都在一张图里
plt.plot(x,y)

plt.figure(num=3,figsize=(8,5)) #num用于对图命名，figsize用于调整图的尺寸
# plt.plot(x,z, label='线条1') #label设置线条的名字
# plt.plot(x,y, color='red', linewidth=1.0,linestyle='--',label='线条2')
#使用图例时，需要采用下面的这种写法
l1, = plt.plot(x,z, label='线条1') #label设置线条的名字
l2, = plt.plot(x,y, color='red', linewidth=1.0,linestyle='--',label='线条2')
#color用于设置时间，linewidth设置线宽，linestyle设置线形


##设置坐标轴
plt.xlim((-1,2)) #设置x轴范围
plt.ylim((-2,3)) #设置y轴范围
plt.xlabel('I am x') #设置x轴名称
plt.ylabel('I am y') #设置y轴名称

#更换x轴和y轴显示的内容
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$', r'$bad\ \alpha$','normal','good','really good'])
#上面r'$really\ bad$', r'$bad\ \alpha$'是用于调整显示的字体和形式，更好看

#修改坐标轴的位置
#gca = get current axis 提取当前坐标轴
ax = plt.gca() #取出当前图像的坐标轴
ax.spines['right'].set_color('none') #spines表示图像的边框，这里right表示右边框，设置其颜色为无
ax.spines['top'].set_color('none')  #设置上边框颜色为无
ax.xaxis.set_ticks_position('bottom') #用下面坐标轴的位置代替x轴的ticks
ax.yaxis.set_ticks_position('left') #用下边坐标轴的位置代替y轴的ticks
ax.spines['bottom'].set_position(('data',-1)) #下面边框的位置改成-1，即-1成为x轴的起始位置而非原点
ax.spines['left'].set_position(('data',0)) #y轴从0开始

##添加图例（即线条的说明）
#添加图例需要首先给每根线条命名，即上面的plt.plot(x,z, label='线条1') #label设置线条的名字
plt.legend(handles=[l1,l2,],labels=['aaa','bbb'],loc='best') #显示图例

##在图中添加注解，文本，图标等


plt.show() #完成所有图像的设置后，需要show()出来这个图像






















