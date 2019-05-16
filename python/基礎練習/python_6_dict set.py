##  2018/12/19 basic_learn_6
##  dict:  字典
##  set:   集合

##key 內容
lang = {
    'name': 'python',
    'type': [1,2,3],
    'typeL': {1:3,3:'A'},
    'version': '3.5'
    }
dict([('name', 'python'), ('version', '3.5')])
print('type:',type(dict),lang)
print(lang['name'])

del lang['name']

lang['b']=20
print(lang)
print(lang['typeL'][3])
