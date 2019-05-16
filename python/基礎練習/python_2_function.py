##  2018/12/18 basic_learn_2
##  function: no return, no return
##  function: global, default parameter
def printdata(s):
    print(s)
def func_add(a,b):
    c = a+b ##it can't return c 
    print('this is a function of add:',a,'+',b,'=',c)
def func_add_return(a,b):
    c = a+b
    return  c
    print('this is a function of add:',a,'+',b,'=',c)##it can't print

a = 20
def func_global():
    global a ##turn to global
    a = a+100
    return  a+100
def sale_car(price,color='red',brand='carmy',is_second_hand=True):
    print('price\t',price,
          'color\t',color,
          'brand\t',brand,
          'is_second_hand\t',is_second_hand
          )
func_add(1,2)
c=func_add_return(1,2)
print('c =',c)
sale_car(100000)
sale_car(1000000,'black','BMW',False)
print('a past=',a)
print(func_global())
print('a now=',a)
a=10
print('a now_2=',a)
func_global()
print('a now_3=',a)
