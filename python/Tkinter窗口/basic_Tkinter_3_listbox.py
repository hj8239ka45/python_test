##  2018/01/12 basic_Tkinter_3
##  listbox
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x150')

var1 = tk.StringVar()
l = tk.Label(window,bg='yellow',width=4,textvariable=var1)
l.pack()

def selection():
    #curselection 選定的值
    value = lb.get(lb.curselection())
    #print(value)
    var1.set(value)

b = tk.Button(window,text='print selection',width=13,height=2,command=selection)
b.pack()

var2 = tk.StringVar()
#設定var2值
var2.set((11,22,33,44))
lb = tk.Listbox(window,listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()

window.mainloop()
