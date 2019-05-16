##  2018/01/12 basic_Tkinter_5
##  scale
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x150')

l = tk.Label(window,bg='yellow',width=20,text='')
l.pack()
#v(隨意假設)自動由scale擷取，因為scale有get value功能
def print(v):
    l.config(text='you have selected'+v)
#從5~11,方向,length pixal寬度,顯示 1 true 0 false,標籤長度
#單位精準度,回應副函式
#HORIZONTAL VERTICAL
#get() : This method returns the current value of the scale.
#set(value) : Sets the scale's value.

s = tk.Scale(window,label='try me',from_=5,to=11,
             orient=tk.HORIZONTAL,length=200,showvalue=0,
             tickinterval=3,resolution=0.001,command=print)
s.pack()
window.mainloop()


def sel():
   selection = "Value = " + str(var.get())
   label.config(text=selection)

window2 = tk.Tk()
window2.title('my window2')
window2.geometry('300x180')
label = tk.Label(window2,bg='yellow',width=20)
label.pack()

var = tk.DoubleVar()

#不傳函數，用tk的var去接，否則則需如同window寫法一致
scale = tk.Scale( window2, variable = var)
scale.pack()

button = tk.Button(window2, text="Get Scale Value", command=sel)
button.pack()

window2.mainloop()
