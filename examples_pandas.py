# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 17:52:14 2021

@author: 28501
"""
#莫烦pandas教程程序
import numpy as np
import pandas as pd

#Class 1
s = pd.Series([1,3,6,np.nan,44,1]) #定义一个一维序列
#如果说numpy是对python列表数据类型的扩展
#那么可以说pandas就是对字典数据类型的扩展
#由上面序列可见，pandas的序列就像字典一样，既有值又有关键字
print(s)
dates = pd.date_range('20210904', periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
df_1 = pd.DataFrame(np.arange(12).reshape((3,4)))
#下载看看源文件怎么写的
print(df_1.dtypes)  #输出列的属性
print(df_1.index) #输出列的序列号
print(df_1.columns) #输出行的
print(df_1.values) #输出值
print(df_1.describe()) 
print(df_1.T)   #转置
print(df_1.sort_index(axis=1,ascending=False))  #排序
#print(df_1.sort_values(by='E'))
print(df_1)
print(df)
print(dates)

#Class 2： 选择数据 
dates_2 = pd.date_range('20210904',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates_2,columns=['A','B','C','D'])
print(df) #以日期排序的，每一列名称以A,B,C,D排序的数组
#选择某一列
print(df['A'],df.A) #两种选择方式
#切片选择
print(df[0:3], df['2021-09-05':'2021-09-07']) #同样是两种选择方式
#根据标签来选择
print(df.loc['2021-09-05']) #按横向标签来选择
print(df.loc[:,['A','B']])   #按纵向标签来选择
print(df.loc['2021-09-05',['A','B']])   #按纵向标签和横向标签来选择
#按位置来选择
print(df.iloc[3])
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])
#按位置和标签综合筛选
#print(df.ix[:3,['A','C']]) #行用位置来选择，列用标签来选择  #新版本已经不可用了
#按布尔条件筛选
print(df[df.A>8])


## 元素赋值，添加，更改
df.iloc[2,2] = 1111
df.loc['20210904','B'] = 2222
df[df.A>4] = 0 
df.A[df.A>4] = 0
df['F'] = np.nan
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20210904',periods=6))
print(df)

## 处理丢失的数据，即NaN数据
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)
print(df.dropna(axis=0,how='any')) #选择丢掉显示行或列中有NaN数据的列表
print(df.dropna(axis=1,how='all')) #0表示行，1表示列，any表示有NaN就丢掉

print(df.fillna(value=0)) #将NaN数据填充成0
print(df.isnull()) #判断数据是否是NaN
print(np.any(df.isnull())==True) #当数据集较大时的判断方法

#数据导入导出
#pandas可以导入：csv,excel,hdf,sql,txt等格式的数据
# data = pd.read_csv('student.csv') #导入csv格式的数据，需先创建student.csv的文件
# print(data)
# data.to_pickle('student.pickle') #保存成名为student.pickle的文件，pickle是pandas常用的文件格式

## 列表的合并
#concatenating 
df_1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df_2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df_3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
print(df_1)
print(df_2)
print(df_3)
#上下合并
result = pd.concat([df_1,df_2,df_3], axis=0)
print(result)
#更新合并后的左侧数据编号，防止重复
print(pd.concat([df_1,df_2,df_3], axis=0,ignore_index=True))

df_4 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'],index=[1,2,3])
df_5 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'],index=[2,3,4])

res = pd.concat([df_4,df_5],join='outer') #join默认是outer,也就是df_4和df_5中
#columns相同的就合并，不同的就置零
print(res)
print(pd.concat([df_4,df_5],join='inner',ignore_index=True)) #inner就是只合并共有的项，非共有的项就删掉

res_2 = pd.concat([df_4,df_5],axis=1,join_axes=[df_4.index]) #新版本已经没有这个参数了
print(res_2)

#append
res_3 =df_4.append([df_2,df_3])



































