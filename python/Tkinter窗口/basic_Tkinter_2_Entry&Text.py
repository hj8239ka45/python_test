##  2018/01/12 basic_Tkinter_2
##  Entry & Text
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x150')

#show輸入後顯示為*
#entry
e = tk.Entry(window,show='●')
e.pack()
def insert_point():
    var = e.get()
    t.insert('insert',var)
def insert_end():
    var = e.get()
    #t.insert('end',var)
    t.insert(1.2,var)

b1 = tk.Button(window,text='insert point',width=13,height=2,command=insert_point)
b1.pack()
b2 = tk.Button(window,text='insert end',width=13,height=2,command=insert_end)
b2.pack()
#text
t = tk.Text(window,height=2)
t.pack()


window.mainloop()
