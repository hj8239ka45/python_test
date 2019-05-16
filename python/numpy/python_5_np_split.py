#2019/3/23
import numpy as np
A=np.arange(12).reshape((3,4))
print(A)
#以列分割成二分
print(np.split(A,2,axis=1))
print(np.hsplit(A,2))
#以橫向分割成二分
print(np.split(A,3,axis=0))
print(np.vsplit(A,3))
