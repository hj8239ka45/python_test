##  2018/12/29 basic_learn_10
##  copy
##  deepcopy
import copy as co
a = [1,2,3]
b = a
print(id(b)) #查在硬碟中的位址
print(id(a))

#位址相同
b[0]=11
print('測試一般b=a:')
print('a',a)
print('b',b)
print('位址是否相同',id(a)==id(b))
print('測試copy結果:')
#copy:矩正位置不相同，但矩正中的矩正位置相同
c = co.copy(a)
print('c',c)
print('位址是否相同',id(a)==id(c))
c[1] = 2222
print('c',c)
print('a',a)
a = [1,2,[3,4]]
print('測試copy二維矩正')
d = co.copy(a)
print('a',a)
print('d',d)
print('id(a),id(d):',id(a)==id(d))
print('id(a[2]),id(d[2]):',id(a[2])==id(d[2]))
a[0] = 11
print('a',a)
print('d',d)
a[2][1] = 13
print('a',a)
print('d',d)
print('測試deepcopy')
#copy:矩正位置不相同，但矩正中的矩正位置不相同
e = co.deepcopy(a)
print('a',a)
print('e',e)
print('id(a[2]),id(e[2]):',id(a[2])==id(e[2]))
