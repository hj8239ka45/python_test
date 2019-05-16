#basic_Tkinter_7_Image
from PIL import ImageTk
from tkinter import *
import PIL
import tkinter as tk
import os
import tkinter.messagebox

class GetCode(object):

    def __init__(self):

        self.data={}  # 存放返回值
        self.window = tk.Tk()
        self.window.geometry('309x230') 
        self.window.resizable(width=False,height=False)   # 固定长宽不可拉伸
        self.textLabel=tk.Label(self.window,text="请输入验证码：").pack() # 标签
        self.textStr=StringVar()
        self.textEntry=tk.Entry(self.window,textvariable=self.textStr)
        self.textStr.set("")
        self.textEntry.pack()  # 输入框

        im=PIL.Image.open("test.jpg")
        img=ImageTk.PhotoImage(im)
        imLabel=tk.Label(self.window,image=img).pack() # 显示图片

        self.but = tk.Button(self.window,text="确认",command=self.return_code).pack(fill="x") # 按键
        self.window.mainloop()

    def return_code(self):
        # 返回输入框内容
        self.data["code"]=self.textStr.get()
        if int(self.data["code"])==1024:
            self.window.destroy()           # 关闭窗体
            print("输入框内容：",self.data["code"])
        #os.remove("test.jpg")         # 删除图片
        else:
            print("錯誤")
            tk.messagebox.showerror(title='Error', message='錯誤')
##            tk.messagebox.showinfo(title='',message='')#提示信息对话窗
##            tk.messagebox.showwarning()#提出警告对话窗
##            tk.messagebox.showerror()#提出错误对话窗
##            tk.messagebox.askquestion()#询问选择对话窗
        
if __name__ == '__main__':
    GetCode()
