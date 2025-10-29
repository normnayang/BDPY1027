import tkinter
from tkinter import font
counter =0
counter2 = [0]
def click():
    global counter
    counter = counter + 1
    lable.config(text="Click %d times"% counter)
def click2():
    counter2[0] += 1
    lable2.config(text="Click %d times"% counter2[0])

top = tkinter.Tk()
for font in font.families():
    print(font)

font1 = tkinter.font.Font(family="Cascadia Code SemiBold",size=24)
font2 = tkinter.font.Font(family="Microsoft JhengHei UI",size=24)
lable = tkinter.Label(top,font=font1,text="This is my first GUI",fg='#000000',bg='#C0FFFF',pady=40)
lable2 = tkinter.Label(top,font=font2,text="中文試看看",fg='#004400',bg='#FFC0EE',pady=30)
button1 = tkinter.Button(top,font=font1,text="Click Me",bg='yellow', command=click)
button2 = tkinter.Button(top,font=font2,text="按下",bg='darkgreen',fg='white',command=click2)
lable2.pack()
lable.pack()
button1.pack()
button2.pack()
top.mainloop()