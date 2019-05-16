##2019/02/24 basic_Tkinter_9_frame
#整潔歸納空間
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x200')

tk.Label(window,text='on the window').pack()
#定義主框架
frm = tk.Frame(window)
frm.pack()
#副框架在主框架下
frm_left = tk.Frame(frm)
frm_right = tk.Frame(frm)
frm_left.pack(side='left')
frm_right.pack(side='right')

tk.Label(frm_left,text='on the frm_l1').pack()
tk.Label(frm_left,text='on the frm_l2').pack()
tk.Label(frm_right,text='on the frm_r1').pack()
tk.Label(frm,text='on the frm_1').pack()

window.mainloop()
