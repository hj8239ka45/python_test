##  2018/12/18 basic_learn_4
##  class:father_son, additional property
##  

class Calculator:
    name = '991E'##initial property
    price = 450
    def __init__(self,name,price,hight=18,width=29,weight=10):##additional property
        self.n = name
        self.p = price
        self.h = hight
        self.wi = width
        self.we = weight
        self.divide(price,hight)
    def add(self,x,y):
        result = x+y
        print(result)
    def times(self,x,y):
        result = x*y
        print(result)
    def minus(self,x,y):
        result = x-y
        print(result)
    def divide(self,x,y):
        result = x/y
        print(result)

c = Calculator('Good Calculator',300,30,15,19)
print('c initial name:\n',c.name)
print('c initial price:\n',c.price)
print('c name now:\n',c.n)
print('c price:\n\r',c.p)
print('c width:\n',c.wi)
c.add(1,5)
c.times(5,5)
d = Calculator('cheap Calculator',200)
print('d name:\n',d.n)
print('d width:\n',d.wi)
##calcul = Calculator() ##used when there's no __init__()term
##print(calcul.name)
##print(calcul.price)
##calcul.add(2,9)
##calcul.times(2,9)
