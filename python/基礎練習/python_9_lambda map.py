##  2018/12/25 basic_learn_9
##  lambda,map
##

a = [1,2,3]
b = [4,5,6]
zip(a,b) #object
c = list(zip(a,b))
print(c)
for i,j in zip(a,b):
    print(i/2,j/2)
d = zip(a,a,b)
def fun1(x,y):
    return (x+y)

fun2 = lambda x,y:x*y #用完即丟，不著痕跡
map(fun1,[1],[2]) #object同zip x=1 y=2
e = list(map(fun1,[1],[2]))
f = list(map(fun1,[1,4],[2,7]))
print(e)
print(f)
