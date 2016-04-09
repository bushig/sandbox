import tkinter
import time
import threading
from random import randint, choice
from tkinter import ttk
top = tkinter.Tk()

top.title('харкач')

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
style.theme_use('classic')
def show_event(event):
    print(event.x)

def test_call_back():
    print('test')
    def callback():
        percent=0
        count = 0
        while percent<100:
            if count == 0:
                start_x = randint(1,1000)
                start_y = randint(1,250)
            else:
                cors=canv.coords(line)
                print(cors)
                start_x = cors[2]
                start_y = cors[3]
            colors = ['red', 'green', 'black', 'purple', 'white',]
            n=randint(0,4)
            print(percent)
            status.config(text='{}% done, {} lines'.format(percent, count))
            percent+=n
            count+=1
            line = canv.create_line(start_x, start_y, randint(1, 1000), randint(1,250), fill=choice(colors), width=3)
            canv.create_oval(start_x-5, start_y-5, start_x+5, start_y+5, fill='black')
            time.sleep(0.1)
        status.config(text='Done!')
    t=threading.Thread(target=callback)
    t.start()
# Code to add widgets will go here...
but=ttk.Button(top, text='Start work', style='TButton', command=test_call_back)
but2=tkinter.Button(top, text='Clack', command=test_call_back)
lab=ttk.Label(top, text='Юникод test', style='BW.TLabel')
checkbox=ttk.Checkbutton(top, text='eqweqe')
canv = tkinter.Canvas(top, width=1000, height=250)
canv.bind('<Button-1>',func=show_event)

status = tkinter.Label(top, text='Ready', bd=1, anchor=tkinter.W, relief=tkinter.SUNKEN)

but.pack()
but2.pack()
lab.pack()
checkbox.pack()
canv.pack()

status.pack(side=tkinter.BOTTOM, fill=tkinter.X)
top.mainloop()