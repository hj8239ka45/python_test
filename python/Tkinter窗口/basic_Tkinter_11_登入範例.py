#登入example
import tkinter as tk
import PIL
from PIL import ImageTk
import tkinter.messagebox
import pickle

class GetCode:
    def __init__(self):

        self.data={}  # 存放返回值
        self.canvas = tk.Canvas(self.window,height=100,width=215)

        im = PIL.Image.open("welcome1.jpg")
        img = ImageTk.PhotoImage(im)
        ##imLabel=tk.Label(window,image=img).pack() # 显示图片

        image = self.canvas.create_image(0,-60,anchor='nw',image=img)
        self.canvas.pack(side='top')
        
        #user info
        self.var_usr_nam = tk.StringVar()
        self.var_usr_nam.set('example@gmail.com')
        self.var_usr_pwd = tk.StringVar()
        tk.Label(self.window,text='User name:').place(x=100,y=120)
        tk.Label(self.window,text='Password:').place(x=100,y=150)
        
        self.usr_nam = tk.Entry(self.window,textvariable=self.var_usr_nam)
        self.usr_nam.place(x=190,y=120)
        self.usr_pwd = tk.Entry(self.window,show='●',textvariable=self.var_usr_pwd)
        self.usr_pwd.place(x=190,y=150)

        #sent butt
        self.but = tk.Button(self.window,text=" Login ",command=self.Login_code)
        self.but.place(x=200,y=180) # 按键
        self.but = tk.Button(self.window,text="Sign up",command=self.Signup_code)
        self.but.place(x=350,y=180) # 按键
        
        self.window.mainloop()
    def Login_code(self):
        # 返回输入框内容
        self.data["code"]=self.var_usr_nam.get()
        self.data["code2"]=self.var_usr_pwd.get()
        try:
            with open('basic_Tkinter_11_usrname.txt', 'r') as file:
                x = file.readlines()
        except FileNotFoundError:
            with open('basic_Tkinter_11_usrname.txt', 'w') as file:
                file.close()
        for i in range(len(x)): #帳號數
            usrnum = len(x[i])-1 #除去\n
            #print(x[i][0:usrnum],'\n',self.data["code"])
            if x[i][0:usrnum]==self.data["code"]:
                #print('username right')
                #print(self.data["code"])
                try:
                    with open('basic_Tkinter_11_pasword.txt', 'r') as file:
                        y = file.readlines()
                except FileNotFoundError:
                    with open('basic_Tkinter_11_pasword.txt', 'w') as file:
                        file.close()
                psdnum = len(y[i])-1
                if y[i][0:psdnum]==self.data["code2"]:
                    #print('password right')
                    tk.messagebox.showinfo(title='Right',message='You can enter!!')#提示信息对话窗
                    #執行下個exe檔或視窗
                    
                    break
            if i==len(x)-1:
                #print("錯誤")
                tk.messagebox.showerror(title='Error',
                message='You have not sign up yet\nor you have wrong number')
                break
    def Signup_code(self):
        #子窗口
        def Signup():
            self.data["code"]=self.var_usr_nam.get()
            self.data["code2"]=self.var_usr_pwd1.get()
            self.data["code3"]=self.var_usr_pwd2.get()
            
            file = open('basic_Tkinter_11_usrname.txt', 'r')
            x = file.readlines()
            for i in range(len(x)): #帳號數
                usrnum = len(x[i])-1 #除去\n
                #print(x[i][0:usrnum],'\n',self.data["code"])
                if x[i][0:usrnum]==self.data["code"]:
                    tk.messagebox.showerror(title='Error',message='This username had been used!!')#提示信息对话窗
                    break
                if self.data["code2"]!=self.data["code3"]:
                    tk.messagebox.showerror(title='Error',message='Second password is diff. with the First!!')#提示信息对话窗
                    break
                if i==len(x)-1:
                    tk.messagebox.showinfo(title='Right',message='Sign up!!')#提示信息对话窗
                    file = open('basic_Tkinter_11_usrname.txt', 'a+')
                    usrname_text = self.data["code"]+'\n'
                    file.write(usrname_text)
                    file.close()
                    file = open('basic_Tkinter_11_pasword.txt', 'a+')
                    psword_text = self.data["code2"]+'\n'
                    file.write(psword_text)
                    file.close()
                    self.window_sign_up.destroy()
        self.window_sign_up = tk.Toplevel(self.window)
        self.window_sign_up.geometry('350x200')
        self.window_sign_up.title('Sign up window')
        
        self.var_usr_nam = tk.StringVar()
        self.var_usr_pwd1 = tk.StringVar()
        self.var_usr_pwd2 = tk.StringVar()
        
        tk.Label(self.window_sign_up,text='User name:').place(x=20,y=20)
        tk.Label(self.window_sign_up,text='Password:').place(x=20,y=50)
        tk.Label(self.window_sign_up,text='Confirm Password:').place(x=20,y=80)
        self.usr_nam = tk.Entry(self.window_sign_up,textvariable=self.var_usr_nam)
        self.usr_nam.place(x=140,y=20)
        self.usr_pwd = tk.Entry(self.window_sign_up,show='●',textvariable = self.var_usr_pwd1)
        self.usr_pwd.place(x=140,y=50)
        self.usr_pwd = tk.Entry(self.window_sign_up,show='●',textvariable = self.var_usr_pwd2)
        self.usr_pwd.place(x=140,y=80)
        #sent butt
        self.but = tk.Button(self.window_sign_up,text="Sign up",command=Signup)
        self.but.place(x=180,y=120)# 按键
    
                
if __name__ =='__main__':
    window = tk.Tk()
    window.title('my window')
    window.geometry('600x400')
    window.resizable(width=False,height=False)   # 固定长宽不可拉伸
        
    GetCode(window)
