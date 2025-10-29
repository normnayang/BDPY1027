import tkinter
from tkinter import font

def func1(e):
    print(e)
def func2(e):
    print(e)

def func3():
    print("Click")


top = tkinter.Tk()

font1 = tkinter.font.Font(family="Cascadia Code SemiBold",size=24)
font2 = tkinter.font.Font(family="Microsoft JhengHei UI",size=24)

label1 = tkinter.Label(top, font=font1, text="Indicator",padx=30,pady=30,bg='#FFC0EE')
button1 = tkinter.Button(top, font=font2, text="按鈕", padx=20,pady=20,bg='#C0FFEE',command=func3)
button1.bind('<Enter>',func1)
button1.bind('<Leave>',func2)
label1.pack()
button1.pack()
top.minsize(600,400)
top.maxsize(1280,720)
top.mainloop()