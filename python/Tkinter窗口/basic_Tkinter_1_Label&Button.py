##  2018/01/12 basic_Tkinter_1
##  Label & Button
import tkinter as tk

#建立窗口
window = tk.Tk()
window.title('my window')
window.geometry('300x150')

#tk的字串變數設定
var = tk.StringVar()
#window上的label
l = tk.Label(window,textvariable=var,bg='green',
             font=('Arial',12),width=15,height=2)
#放置位置
#l.pack()相對
#l.place()具體的點
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        l.pack()
        var.set('you hit me')
    else:
        on_hit = False
        l.forget()

#window上的Button,command為運行函數
b = tk.Button(window,text='hit me',width=15,height=2,command=hit_me)
b.pack()

window.mainloop()
