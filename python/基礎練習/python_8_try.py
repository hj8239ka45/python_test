##  2018/12/25 basic_learn_8
##  try
##
try:
    file = open('eeee.txt','r+')
except Exception as e:
    print('there is no file named as eeee')
    response = input('do you want to create a new file: \n')
    if response == 'y':
        file = open('eeee.txt','w')
    else:
        pass
else:
    file.write('ssss')
    file.close()
