import tkinter
from tkinter import font

def motionCallback(e):
    message1.config(text="move to:{}".format((e.x,e.y)))


top = tkinter.Tk()

font1 = tkinter.font.Font(family="Cascadia Code SemiBold",size=24)
font2 = tkinter.font.Font(family="Microsoft JhengHei UI",size=24)

message1 = tkinter.Message(top, text="record path", font=font1,bg="#C0FFEE")
message1.pack()
top.bind('<Motion>',motionCallback)
top.minsize(600,400)
top.maxsize(1280,720)
top.mainloop()