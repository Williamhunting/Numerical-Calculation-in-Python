#根据莫烦的数据处理教程写的关于numpy和pandas使用的程序


import numpy as np

#矩阵定义
array1 = [[1,2,3],[2,3,4]] #如果采用这种方式，则定义的只是一个多维列表
array2 = np.array([[1,2,3],[2,3,4]]) #这样才是一个numpy的矩阵
print(array1)
print(array2) #可以看到，numpy的矩阵输出的元素之间没有逗号间隔
#矩阵性质显示
print('number of dim:',array2.ndim) #输出矩阵的维度，看来就是行数
print('shape:',array2.shape)  #输出矩阵的行数和列数
print('size:',array2.size)  #输出矩阵元素的个数

a = np.array([2,23,4],dtype=np.int64)  #dtype用于定义矩阵元素的格式
#dtype 可以选择float32, float64等等
print(a.dtype)

#快速定义一些特定矩阵
a = np.zeros((3,4)) #定义指定行数和列数的零矩阵
b = np.ones((3,4))  #定义指定行和列的一矩阵
c = np.empty((3,4))  #定义指定行和列的元素极小的矩阵
d = np.arange(10,20,2) #定义一个起始值10，末尾值20，步长2的矩阵
e = np.arange(12).reshape((3,4)) #定义一个3行4列的从0到11的矩阵
#np.arange与python自带的range()函数类似
f = np.linspace(1,20,10) #定义将1到20平均分成10段的矩阵
#np.linspace(1,20,10).reshape((2,3)) 也可以添加reshape更改矩阵的样式
print(f)


#矩阵的基本运算
aa = np.array([10,20,30,40])
bb = np.arange(4)
#矩阵减法
cc = aa - bb  #逐个元素相减
#矩阵加法
dd = aa + bb
#矩阵元素平方
ee = aa**2 # 各元素的平方
ff = 10*np.sin(aa)  #三角函数运算 
print(bb)
print(bb<3) #返回矩阵中小于指定值的矩阵，是一个True或False组成的矩阵
#类似的，可以写print(bb==3), print(bb>3)

gg = np.array([[1,1],[0,1]])
hh = np.arange(4).reshape((2,2))
#矩阵元素相乘
ii = gg*hh 
#矩阵相乘
jj = np.dot(gg,hh)#ii.dot(jj)和ii@jj这两种写法也表示矩阵乘法
jj_2 =  gg.dot(hh)
print(ii)
print(jj)

kk = np.random.random((2,4))
print(kk)
print(np.sum(kk)) #矩阵元素求和
print(np.min(kk)) #矩阵元素的最小值
print(np.max(kk)) #矩阵元素的最大值
print(np.sum(kk,axis=1)) #矩阵每一行求和   0表示列，1表示行
print(np.min(kk,axis=0)) #矩阵每一列的最小值 
print(np.max(kk,axis=1)) #矩阵每一行的最大值

A = np.arange(2,14).reshape((3,4))

print(np.argmin(A)) #最小值的索引
#索引返回的是将矩阵作为一列数列来看的最小值在数列中的位置
print(np.argmax(A)) #最大值的索引
print(np.mean(A))  #A.mean()也可以
print(np.mean(A,axis=0)) #求每一列的平均值
print(np.average(A)) #也是求均值
print(np.median(A)) #输出中位数
print(np.cumsum(A)) #输出每个元素是前面元素累加值的数列
print(np.diff(A)) #输出当前元素和前一个元素做差的矩阵
print(np.nonzero(A)) #输出所有非零数的索引
print(np.sort(A))  #对矩阵排序

print(np.transpose(A))  #矩阵转置
print(A.T) #矩阵转置的第二种写法

print(np.clip(A,5,9)) #所有9的数都变成9，所有小于5的数都变成5，之间的值不变
print(A)

#矩阵的索引
B = np.arange(3,15)
print(B)
print(B[2])
B_2 = np.arange(3,15).reshape((3,4))
print(B_2)
print(B_2[2])
print(B_2[2,:]) #取矩阵行或者列索引的第二种方法
print(B_2[1,1:2]) #取矩阵行或列的部分元素，即切片操作
print(B_2[1][1])
print(B_2[1,1]) #取矩阵元素索引的第二种方法

for row in B_2: #采用循环输出矩阵的每一行
    print(row)

for column in B_2.T: #转置之后即可循环矩阵的每一列
    print(column)
    
print(B_2.flatten()) #flatten和下面flat稍有区别
#flatten是修改了矩阵的样式成为一个一维的矩阵，而flat只是一个迭代器，使得
#矩阵可以按元素循环，并不改变矩阵的样式
for item in B_2.flat: #将矩阵转变成一个数列之后即可循环每个元素
    print(item)

##矩阵的合并
C = np.array([1,1,1])
D = np.array([2,2,2])
E = np.vstack((C,D)) #vertical stack, 上下合并
F = np.hstack((C,D)) #horizontal stack, 左右合并
print(F.shape,E.shape)  
#把一个横向的数列改成竖向的数列，因为采用转置是不行的
print(C.T)  #转置不能把横向数列变成竖向数列
#需要先在列上增加一个维度
#print(C[np.newaxis,:])  #在行上增加一个维度
print(C[:,np.newaxis]) #在列上增加一个维度

G = np.hstack((C[:,np.newaxis],D[:,np.newaxis]))
print(G)

H = np.concatenate((C[:,np.newaxis],D[:,np.newaxis],D[:,np.newaxis],C[:,np.newaxis]),axis=1) #这个函数可以进行多个矩阵的合并,
#并指定合并的方向，axis=0是纵向（列）合并，1是横向合并
print(H)

## 矩阵的分割
I = np.arange(12).reshape((3,4))
print(I)
print(np.split(I,2,axis=1)) #分割成2块，在列的方向上进行
print(np.split(I,3,axis=0)) #分割成3块，在行的方向进行
#或者采用：
print(np.vsplit(I,3))  #纵向分割 
print(np.hsplit(I,2))  #横向分割

#以上都是等量分割，下面是不等量分割
#print(np.split(I,3,axis=1)) #不等量分割，会报错
print(np.array_split(I,3,axis=1))  #采用array_split就可进行不等量分割

##矩阵的赋值和复制
J = np.arange(4)
#浅复制，即只是定义一个变量的别名
K = J #采用这种等号的定义，表示K就是J,两者指向同一个变量，即改变其中一个就改变了两个
L = J
M = K
J[0] = 11
print(J)
print(K is J)      #判断两个变量是否指向同一个变量
#深复制，即复制一个完全无关的，仅值相同的变量
N = J.copy() #深复制,弹幕也有讲这也不是真的深拷贝，还可再看看相关材料

print(np.nan)  #NaN














#x = np.empty([3,2], dtype = int)
#print(x)
