##  2018/12/18 basic_learn_3
##  files: w & a need to close file
##  files: r no need to close file
text = 'This is my first text.\r\nThis is my second text.\r\n'
print(text);

##
F = open('my file.txt','w')
print(F,'\r\n');
F.write(text)
F.close()

text = 'This is my Third text.\r\nThis is my Fourth text.\r\n'
##
my_file = open('my file.txt','a+')
print(my_file,'\r\n');
my_file.write(text)
my_file.close()

##
file = open('my file.txt', 'r')
print('file.readlines:\n',file.readlines()) ##put the fileread in list for all


##
file = open('my file.txt', 'r')
print('file.readline:\n',file.readline()) ##put the fileread in list for one line


##
file = open('my file.txt', 'r') 
for line in file: 
    print('file_for:',line)

##
file = open('my file.txt', 'r') 
content = file.read()
print('file._content:\n',content)
