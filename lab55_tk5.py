import tkinter
from tkinter import font

'''def command1():
    label1.config(text="iPhone")

def command2():
    label1.config(text="Android")'''

def command():
    if selector.get() == 1:
        label1.config(text="iPhone")
    elif selector.get() == 2:
        label1.config(text="Android")


top = tkinter.Tk()
selector = tkinter.IntVar()
selector.set(2)

font1 = tkinter.font.Font(family="Cascadia Code SemiBold",size=24)
font2 = tkinter.font.Font(family="Microsoft JhengHei UI",size=24)

label1 = tkinter.Label(top,text="Hello World", font=font1)

rb1 = tkinter.Radiobutton(top,text="Apple", font=font2,value=1,command=command,variable=selector)
rb2 = tkinter.Radiobutton(top,text="Google", font=font1,value=2,command=command,variable=selector)

label1.pack()
rb1.pack()
rb2.pack()
top.minsize(600,400)
top.maxsize(1280,720)
top.mainloop()