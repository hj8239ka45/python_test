from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import tkinter as tk
import os
#import easygui
from tkinter.filedialog import askopenfilename as askopfile

class GetCode:    
    def __init__(self, windows=None):
        self.window = window
        self.data={}  # 存放返回值
        self.var_port = tk.StringVar()
        self.var_port.set('5020')
        e = tk.Entry(self.window,textvariable=self.var_port,font=('Arial',12)).place(x=60,y=20)
        self.var_report = tk.StringVar()
        self.var_report.set('port: ')
        l1 = tk.Label(self.window,textvariable=self.var_report,font=('Arial',12)).place(x=20,y=20)

        self.var_ip = tk.StringVar()
        self.var_ip.set('127.0.0.1')
        e = tk.Entry(self.window,textvariable=self.var_ip,font=('Arial',12)).place(x=60,y=60)
        self.var_reip = tk.StringVar()
        self.var_reip.set('IP: ')
        l2 = tk.Label(self.window,textvariable=self.var_reip,font=('Arial',12)).place(x=20,y=60)
        b = tk.Button(self.window,text='enter',width=13,height=2,command=self.enter).place(x=100,y=100)
    def enter(self):
        self.data["port"] = self.var_port.get()
        self.data["ip"] = self.var_ip.get()
        print(self.data["port"],self.data["ip"])
        client = ModbusClient(self.data["ip"], self.data["port"])

        self.window_connect = tk.Toplevel(self.window)
        self.window_connect.geometry('380x400')
        self.window_connect.title('Connected window')
        self.window_connect.resizable(width=False,height=False)
        #filemenu
        def close():
            client.close()
            self.window_connect.destroy()   #self.window_connect.withdraw()
        def openfile():            
            #path = easygui.fileopenbox()
            default_dir = os.getcwd()
            fname = askopfile(
                filetypes=(("Excel 活頁簿","*.xlsm*;*.xlsx*;*.xls*"),
                               ("Excel 4.0活頁簿","*.xlst*;*.xlw*"),
                               ("python","*.py")),
                        title="选择文件",
                        initialdir=(os.path.expanduser(default_dir))
                )
            #os.system("start "+fname) ##open document
            
        menubar = tk.Menu(self.window_connect)
        filemenu = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='Connect',menu=filemenu)
        filemenu.add_command(label='Close',command=close)
        self.window_connect.config(menu=menubar)
        
        filemenu2 = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='File',menu=filemenu2)
        filemenu2.add_command(label='Open',command=openfile)
        
        def pr_select():
            trans_type = self.var.get()
            print(trans_type)
            if trans_type=='DO':
                lp.place(x=140,y=130)
                ep.place(x=180,y=130)
                lq.place(x=240,y=130)
                eq.place(x=300,y=130)
            else:
                print('else')
                lp.place_forget()
                lq.place_forget()
                ep.place_forget()
                eq.place_forget()
        def sent():
            trans_type = self.var.get()
            input_data = self.var_input.get()
            print(bool(input_data))
            if trans_type == 'AO':
                rq = client.write_registers(0, input_data, unit=1)
            elif trans_type == 'DO':
                quanti = self.var_Qinput.get()
                position = self.var_Pinput.get()
                rq = client.write_coils(position, [bool(input_data)]*quanti, unit=1)
            elif trans_type == 'SDO':#只改第一個coil
                rq = client.write_coil(0, bool(input_data), unit=1)
            print('get:',trans_type,input_data)
            #holding registers(hr):
            rr = client.read_holding_registers(0,2, unit=1) #read AO
            A = rr.registers
            #discrete inputs(di):
            rr = client.read_discrete_inputs(0, 8, unit=1)  #will reply 1 byte --> 8 bits
            B = rr.bits
            #coil read(co):
            rr = client.read_coils(0, 8, unit=1)            #被數到的打開遮罩，沒數到的被遮罩
            C = rr.bits
            #input registers(ir):
            rr = client.read_input_registers(0,2, unit=1)   #read AI
            D = rr.registers    
            self.var_l3.set(A)
            self.var_l4.set(B)
            self.var_l5.set(C)
            self.var_l6.set(D)
            
        self.var_l2 = tk.StringVar()
        self.var_l2.set('trans. protocol : ')
        l2 = tk.Label(self.window_connect,textvariable=self.var_l2,font=('Arial',12)).place(x=20,y=20)
        

        self.var_Lposition = tk.IntVar()
        self.var_Lposition.set('posi. : ')
        lp = tk.Label(self.window_connect,textvariable=self.var_Lposition,font=('Arial',12))
        self.var_Pinput = tk.IntVar()
        ep = tk.Entry(self.window_connect,textvariable=self.var_Pinput,font=('Arial',12),width=5)

        self.var_quanti = tk.IntVar()
        self.var_quanti.set('quanti. : ')
        lq = tk.Label(self.window_connect,textvariable=self.var_quanti,font=('Arial',12))
        self.var_Qinput = tk.IntVar()
        eq = tk.Entry(self.window_connect,textvariable=self.var_Qinput,font=('Arial',12),width=5)
        
            
                    
        self.var = tk.StringVar()
        r1 = tk.Radiobutton(self.window_connect,text='Analog Output',variable=self.var,value='AO',command=pr_select).place(x=160,y=40)
        r2 = tk.Radiobutton(self.window_connect,text='Multi Digital Output',variable=self.var,value='DO',command=pr_select).place(x=160,y=70)
        r4 = tk.Radiobutton(self.window_connect,text='Single Digital Output',variable=self.var,value='SDO',command=pr_select).place(x=160,y=100)

        self.var1 = tk.StringVar()
        self.var1.set('say sth. : ')
        l1 = tk.Label(self.window_connect,textvariable=self.var1,font=('Arial',12)).place(x=20,y=130)
        self.var_input = tk.IntVar()
        e = tk.Entry(self.window_connect,textvariable=self.var_input,font=('Arial',12),width=5).place(x=80,y=130)
        
        b = tk.Button(self.window_connect,text='sent',width=13,height=2,command=sent).place(x=100,y=170)
            
        self.var2 = tk.StringVar()
        self.var2.set('holding registers :')#read/write 1bit bool
        l3 = tk.Label(self.window_connect,textvariable=self.var2,font=('Arial',12)).place(x=20,y=220)
        self.var_l3 = tk.StringVar()
        self.var_l3.set('')
        l3 = tk.Label(self.window_connect,textvariable=self.var_l3,font=('Arial',12)).place(x=160,y=220)
 
        self.var3 = tk.StringVar()
        self.var3.set('discrete Input :')#read 1bit  bool
        l4 = tk.Label(self.window_connect,textvariable=self.var3,font=('Arial',12)).place(x=20,y=250)
        self.var_l4 = tk.StringVar()
        self.var_l4.set('')
        l4 = tk.Label(self.window_connect,textvariable=self.var_l4,font=('Arial',12)).place(x=160,y=250)

        self.var4 = tk.StringVar()
        self.var4.set('coil :')#read
        l5 = tk.Label(self.window_connect,textvariable=self.var4,font=('Arial',12)).place(x=20,y=280)
        self.var_l5 = tk.StringVar()
        self.var_l5.set('')
        l5 = tk.Label(self.window_connect,textvariable=self.var_l5,font=('Arial',12)).place(x=160,y=280)

        self.var5 = tk.StringVar()
        self.var5.set('input registers :')#read/write
        l6 = tk.Label(self.window_connect,textvariable=self.var5,font=('Arial',12)).place(x=20,y=310)
        self.var_l6 = tk.StringVar()
        self.var_l6.set('')
        l6 = tk.Label(self.window_connect,textvariable=self.var_l6,font=('Arial',12)).place(x=160,y=310)
     

if __name__ == '__main__':
    window = tk.Tk()
    window.title('my modbus')
    window.geometry('300x150')
    window.resizable(width=False,height=False)
    GetCode(window)
    
    window.mainloop()
