import socket
name = socket.gethostname()#取得此電腦ip下名稱
print (name)
##ip = socket.gethostbyname(name)#取得名稱下ip
ip = '192.168.43.160'
client = socket.socket()
port = 1234
client.connect((ip.encode(),port))

