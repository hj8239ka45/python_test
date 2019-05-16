import tkinter as tk
import tkinter.messagebox
import socket
import sys

window = tk.Tk()
window.title('my socket_client')
window.geometry('300x150')
window.resizable(width=False,height=False)


data={}  # 存放返回值

var_port = tk.IntVar()
var_port.set('1234')
e = tk.Entry(window,textvariable=var_port,font=('Arial',12)).place(x=60,y=20)
var_report = tk.StringVar()
var_report.set('port: ')
l1 = tk.Label(window,textvariable=var_report,font=('Arial',12)).place(x=20,y=20)


var_ip = tk.StringVar()
var_ip.set('192.168.43.160')
e = tk.Entry(window,textvariable=var_ip,font=('Arial',12)).place(x=60,y=60)
var_reip = tk.StringVar()
var_reip.set('IP: ')
l2 = tk.Label(window,textvariable=var_reip,font=('Arial',12)).place(x=20,y=60)
    
def enter():
    name = socket.gethostname()

    print (name)
    client = socket.socket()
    data["port"] = var_port.get()
    data["ip"] = var_ip.get()
    print(data["port"],data["ip"])
    
    try:
        client.connect((data["ip"].encode(),data["port"]))

        window_connect = tk.Toplevel(window)
        window_connect.geometry('300x200')
        window_connect.title('Connected window')
        window_connect.resizable(width=False,height=False)
        menubar = tk.Menu(window_connect)
        def close():
            print(client)
            client.close()
            window_connect.destroy()
        
        filemenu = tk.Menu(menubar,tearoff=1)
        menubar.add_cascade(label='Connect',menu=filemenu)
        filemenu.add_command(label='Close',command=close)
        window_connect.config(menu=menubar)

        var_client = tk.StringVar()
        var_client.set('')
        ec = tk.Entry(window_connect,textvariable=var_client,font=('Arial',12)).place(x=80,y=20)
        var_client2 = tk.StringVar()
        var_client2.set('client: ')
        l1 = tk.Label(window_connect,textvariable=var_client2,font=('Arial',12)).place(x=20,y=20)


        var_server = tk.StringVar()
        var_server.set('')
        ls = tk.Label(window_connect,textvariable=var_server,font=('Arial',12)).place(x=80,y=60)
        var_server2 = tk.StringVar()
        var_server2.set('server: ')
        l2 = tk.Label(window_connect,textvariable=var_server2,font=('Arial',12)).place(x=20,y=60)

        def sent():
            data["client"] = var_client.get()
            client.send(data["client"].encode())
            #data["server"] = client.recv(1024).decode()
            redata = client.recv(1024).decode()
            print(redata)
            var_server.set(redata)
        b = tk.Button(window_connect,text='sent',width=13,height=2,command=sent).place(x=130,y=100)
    except:
        print("ConnectionRefusedError: [WinError 10061] 無法連線，因為目標電腦拒絕連線。")
        tk.messagebox.showerror(title='Error',message='Connection Refused Error!!')
        sys.exit()
b = tk.Button(window,text='connect',width=13,height=2,command=enter).place(x=100,y=100)
window.mainloop()
