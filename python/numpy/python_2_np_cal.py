#108/3/16
import numpy as np
import math
#np中axis=0 =1 運算中皆存在
a = np.array([10,20,30,40])
b = np.arange(4)

print(a,'\n',b)
print(b<3)
c = a-b
print(c)

for i in range(1,5):
    d = np.sin(math.pi/5*i,dtype=np.float)
    print(d)

aa = np.array([[1,1],[0,1]])
bb = np.arange(4).reshape((2,2))
cc = aa*bb
#矩正運算
cc_dot = np.dot(aa,bb)
cc_dot2 = aa.dot(bb)
print(cc)
print(cc_dot)
print(cc_dot2)

#0~1亂數
a = np.random.random((2,4))
print('\n\n',a)
#axis = 1列數求  =0行數求
print(np.sum(a,axis=1))
print(np.min(a,axis=0))
print(np.max(a))

#最大小值的索引
A = np.arange(14,2,-1).reshape((3,4))
print('\n\n',np.argmin(A))
print(np.argmax(A))
print(np.average(A))#print(A.argmean()) print(np.average(A)) print(A.average())
#累加上去
print(np.cumsum(A))
#前後相差
print(np.diff(A))
#排序
print('\n\n',np.sort(A))
print(np.transpose(A))#print((A.T))
#大於9=9 小於5=5
print(np.clip(A,5,9))

