import tkinter
from tkinter import font


def updateText(event):
    label1.config(text=entry1.get())

top = tkinter.Tk()

font1 = tkinter.font.Font(family="Cascadia Code SemiBold",size=24)
font2 = tkinter.font.Font(family="Microsoft JhengHei UI",size=24)
label1 =tkinter.Label(top,text="your input is",font=font1)
entry1 = tkinter.Entry(top,font=font2,width=40)
button1 = tkinter.Button(top,text="ok",font=font2,width=40)
label1.pack()
entry1.pack()
button1.pack()
entry1.bind('<Return>',updateText)
button1.bind('<Button-1>',updateText)
top.minsize(600,400)
top.maxsize(1280,720)
top.mainloop()