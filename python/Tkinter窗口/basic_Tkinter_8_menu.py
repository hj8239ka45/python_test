##  2018/02/23 basic_Tkinter_8
##  menu
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x200')

l = tk.Label(window,text='',bg='yellow')
l.pack()

counter = 0
def do_job():
    global counter
    counter +=1
    l.config(text='do'+str(counter))
    

    
menubar = tk.Menu(window)
#filemenu

    #tearoff外拉功能表
filemenu = tk.Menu(menubar,tearoff=1)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_command(label='Exit',command=window.quit)
    #separator分隔線
filemenu.add_separator()

#editmenu
editmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

#submenu
submenu=tk.Menu(filemenu,tearoff=0)
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
submenu.add_command(label='Submenu1',command=do_job)
submenu.add_command(label='Submenu2',command=do_job)

window.config(menu=menubar)
window.mainloop()
