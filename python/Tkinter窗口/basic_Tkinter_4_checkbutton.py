import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x200')
def print_selection():
    #改變l的config(參數)
    var = var1.get()+var2.get()
    if(var==2):
        l.config(text='I love both')
    elif(var==1):
        if(var1.get()==1):
            l.config(text='I love Pyhton')
        else:
            l.config(text='I love C++')
    else:
        l.config(text='I do not love either')
    
#variable的值var會去複製value的內容
#按下後直接讀取(radiobutton呼叫print_selection的method)
    
var1 = tk.IntVar()
var2 = tk.IntVar()
l = tk.Label(window,bg='yellow',width=20,height=2
             ,text='empty')
l.pack()

c1 = tk.Checkbutton(window,text='Python',
                    variable=var1,onvalue=1,
                    offvalue=0,command=print_selection)
c1.pack()

c2 = tk.Checkbutton(window,text='C++',
                    variable=var2,onvalue=1,
                    offvalue=0,command=print_selection)
c2.pack()


window.mainloop()
