##  2018/01/12 basic_Tkinter_6
##  canvas畫布
import tkinter as tk
import PIL
from PIL import ImageTk

window = tk.Tk()
window.title('my window')
window.geometry('300x200')

canvas = tk.Canvas(window,bg='blue',height=100,width=200)

im=PIL.Image.open("image.jpg")
img=ImageTk.PhotoImage(im)
##imLabel=tk.Label(window,image=img).pack() # 显示图片

image = canvas.create_image(0,0,anchor='nw',image=img)

x0,y0,x1,y1=50,50,80,80
line = canvas.create_line(x0,y0,x1,y1,fill='red')
arc = canvas.create_oval(x0,y0,x1,y1,fill='red')
#start,extent角度
arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=180,fill='red')
rect = canvas.create_rectangle(100,30,100+30,50)
canvas.pack()

def moveit():
    canvas.move(rect,0,2)
b = tk.Button(window,text='move',command=moveit).pack()

window.mainloop()
