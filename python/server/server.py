import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())

port = 1234
address = (ip,port)
server.bind(address)
server.listen(1)
print ("[*] STARTED LISTENING ON ",ip,":",port)
client,addr = server.accept()
print ("[*] GOT A CONNECTION FROM ",addr[0],":",addr[1])
client.send("START TO COMMUNICATE".encode())
while True:
    data = client.recv(1024)
    data = data.decode()
    print ("[*] RECEIVED",data,"FROM THE CLIENT")
    print ("	PROCESSING DATA")
    print (data,type(data))
    
    client.send("I got it.".encode())
    print("	    PROCESSING DONE.\n[*] REPLY SENT")
    
    if(data=="hello server "):
        client.send("hello client".encode())
        print("	    PROCESSING DONE.\n[*] REPLY SENT")
    elif(data=="disconnect  "):
        client.send("goodbye".encode())
        client.close()
        break
##    else:
##        client.send("Invalid data".encode())
##        print("     PROCESSING DONE INVALID DATA.\n[*] REPLY SENT")
