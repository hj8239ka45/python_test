import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname("www.google.com")
print (ip)
port = 80
address=(ip,port)
client.connect(address)

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())
data = client.recv(1024)
data = data.decode()
print(data)
