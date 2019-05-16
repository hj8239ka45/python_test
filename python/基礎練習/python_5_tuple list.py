##  2018/12/19 basic_learn_5
##  tuple: 元組...不可以修改！不可以刪除！
##  list:  串列...改變元素值的方法:list.pop(),list.reverse(),list.append()....
##  多維列表[[],[]]

a_tuple = (12,3,5,15,6)
another_tuple = 1,2,3,44,8,99,22

a_list = [[1,3,5,7,9],[0,2,4,6,8]]

print(a_tuple)
print(a_list)

##the number taken from a_list is put into the content one by one
for content in a_list:
    print(content)
for y_index in range(len(a_list)):## the type of range is tuple
    for x_index in range(len(a_list[y_index])):
        print('index =',x_index,',',y_index,'\tnumber in list= ',a_list[y_index][x_index])





languages = ['python', 'js', 'go']
print('origin languages:',languages);#['python', 'js', 'go']

#add the unit in the last one of list
languages.append('java')    #['python', 'js', 'go', 'java']
print('append\nlanguages:',languages)

#series the list by extend (it will add by extending term)
languages.extend('c-')  #['python','js','go','c','-']
print('extend\nlanguages:',languages)
languages += [ 'python', 'python','ruby', 'c++'] #['python','js','go','java','c','-','python','python','ruby','c++']
print('add\nlanguages:',languages)

#insert unit into selected index
languages.insert(2, 'matlab') #['python', 'js', 'matlab', 'go', 'java', 'c', '-', 'python', 'python', 'ruby', 'c++']
print('insert\nlanguages:',languages)

#delete selected index unit -2:count from the last
del languages[-6:-4] #['python','js','matlab','go','java','python','python','ruby','c++']
print('del\nlanguages:',languages)

#remove selected frontest unit
languages.remove('js')
languages.remove('java')
languages.remove('python')#['matlab','go','python','python','ruby','c++']
print('remove\nlanguages:',languages)
print('languages[-3:]:',languages[-3:])#['python', 'ruby', 'c++']
print('matlab' in languages) # True
print('ruby' in languages) # False

#index
print('index of go:',languages.index('go'))

#count times
print('count of python:',languages.count('python'))

#sort: rearrange from low to high Or reverse
languages.sort()
print('sort\tlanguages:',languages)
languages.sort(reverse = True)
print('reverse sort languages:',languages)

#join
string = '-'
a=string.join(languages)
print('join -\tlanguages:',a)

