import tkinter
from tkinter import font

def func1(e):
    print('e=',e)
    label.config(text="change value to {}".format(e))

top = tkinter.Tk()

font1 = tkinter.font.Font(family="Cascadia Code SemiBold",size=24)
font2 = tkinter.font.Font(family="Microsoft JhengHei UI",size=24)
label = tkinter.Label(top,text="scale value=??",font=font1)
label.pack()
scale = tkinter.Scale(top,orient='horizontal',from_=0,to=100,font=font2,command=func1)
scale.pack(fill='x')
top.minsize(600,400)
top.maxsize(1280,720)
top.mainloop()