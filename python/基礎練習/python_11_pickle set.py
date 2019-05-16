##  2018/12/29 basic_learn_11
##  pickle: 保存結果的檔案('方便以後加工)
##  set:找不同
import pickle
a_dict = {'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}
with open('pickle_example.pickle','wb') as file:#'wb':保存形式 寫入byte
    pickle.dump(a_dict,file)#倒入資料

with open('pickle_example.pickle','rb') as file:#自動關閉
    a_dict1 = pickle.load(file)
print(a_dict1)


##
char_list = ['a','b','c','c','d','d','d']
sentence = 'Welcome Back to This Tutorail'

print(set(char_list))
print(set(sentence))
print(type(set(char_list)))
print(type(char_list))

unique_char = set(char_list)
unique_char.add('x')
unique_char.add('a')
print(unique_char)
print(type(unique_char))
print(unique_char.remove('x'))#刪除
print(unique_char)
print(unique_char.discard('y'))#刪除，沒有元素沒關係
#print(unique_char.clear())#清除

set1 = unique_char
set2 = {'a','e','i'}
print(set1.difference(set2))
print(set1.intersection(set2))
