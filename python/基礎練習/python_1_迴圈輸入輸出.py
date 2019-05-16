##  2018/12/18 basic_learn_1
##  print
##  while
##  for: range
##  if,elseif,else
##  input

add = 12;
a,b,c=1,2,3
print(add)
print(a,b,c)
condition = 0
a_input = input('please give a number:')
print('This input number is:',a_input)
while condition < 10:
    print(condition)
    condition = condition+1
##ctrl + shift +z =inverse ctrl+z
##ctrl + alt +] =tab
##ctrl + alt +[ =/tab
example = [1,2,3,4,5,6,777,88,265]
for i in example:
    print(i)
    print('inner of for')
print('out of for')
## 123  alt+3註解 alt+4取消註解
## alt +D+G 跳行數
## alt + M 打開改模塊的py源碼供瀏覽
for i in range(0,10,2):##0~9
    print(i)
x=1
y=2
z=3
if x<y<z:
    print('x is less than y, and y is less than z')
else:
    print('x is greater than y,or y is greater than z')
z=0
if x<y>z:
    print('x is less than y, and y is greater than z')
y=1
z=1
if x!=y:
    print('x is not equal to y')
elif x==z:
    print('x is equal to z')
else:
    print('x is equal to y')
##    else
##    print('x is less than y')
