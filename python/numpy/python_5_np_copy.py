#2019/3/23
import numpy as np
a=np.arange(4)
b=a
c=a
d=b
if(b is a):
    print("b 跟 a的記憶體相同")
else:
    print("b is different with a")
#想要值但不想要同記憶體 deepcopy
b=a.copy()
print('After deepcopy:')
if(b is a):
    print("b 跟 a的記憶體相同")
else:
    print("b is different with a")
