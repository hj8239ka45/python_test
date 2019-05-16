#2019/3/23 combine
import numpy as np

A=np.array([1,1,1])
B=np.array([2,2,2])
#vertical stack 垂直合併
C=np.vstack((A,B))
#horizontal stack 水平合併
D=np.hstack((A,B))
print(A.shape,C.shape,D.shape) #print(A,C)
print(D)

#橫向數列不能用T轉束向數列
print('\n',A.T.shape)


#使用加維度後再轉矩陣，或直接定義加哪一方向維度
A=A[:,np.newaxis]
B=B[:,np.newaxis]
print('\n',A.shape)
print(A)

#多個縱向橫向矩陣合併,axis=0縱向 =橫向
E=np.concatenate((A,B,B,A),axis=1)
print('\n',E)
