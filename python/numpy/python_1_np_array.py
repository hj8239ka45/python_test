#108/3/16
import numpy as np
#定義形式
array = np.array([[1,22,3],[2,3,4]],dtype=np.int64)
print(array)
print(array.dtype)
print('number of dim:',array.ndim)
print('shape:',array.shape)
print('size:',array.size)

a = np.zeros((3,4))
print('\n',a)
a = np.ones((3,4),dtype=np.int64)
print('\n',a)
a = np.empty((3,4),dtype=np.float)
print('\n',a)
#10~20每2
a = np.arange(10,20,2)
print('\n',a)

#3行4列
a = np.arange(12).reshape((3,4))
print('\n',a)

a = np.linspace(1,10,6).reshape((3,2))
print('\n',a)
