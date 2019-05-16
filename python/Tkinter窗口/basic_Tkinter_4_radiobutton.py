##  2018/01/12 basic_Tkinter_4
##  radiobutton
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x150')


var = tk.StringVar()
l = tk.Label(window,bg='yellow',width=20,height=2
             ,text='')
l.pack()

def print_selection():
    #改變l的config(參數)
    l.config(text='you had selected '+var.get())

    
#variable的值var會去複製value的內容
#按下後直接讀取(radiobutton呼叫print_selection的method)
r1 = tk.Radiobutton(window,text='Option A',
                    variable=var,value='A',
                    command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window,text='Option B',
                    variable=var,value='B',
                    command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window,text='Option C',
                    variable=var,value='C',
                    command=print_selection)
r3.pack()

window.mainloop()
