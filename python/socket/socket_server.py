import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 1234
address=(ip,port)
server.bind(address)
server.listen(3)
print("[*] Started listening on ",ip,":",port)
client,addr = server.accept()
print("[*] Got a connection from ",addr[0],":",addr[1])
while True:
    data = client.recv(1024)
    data = data.decode()
    print("[*] Received ",data," from the client")
    print("  processing data")
    if(data=="goodbye"):
        client.send(("goodbye").encode())
        client.close()
    elif(data=="hallo server"):
        client.send(("hallo client").encode())
    else:
        client.send(data.encode())
