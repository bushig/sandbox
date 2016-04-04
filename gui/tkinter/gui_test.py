import tkinter
from tkinter import ttk
top = tkinter.Tk()

top.title('харкач')

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
style.theme_use('classic')

def test_call_back():
    print('test')
# Code to add widgets will go here...
but=ttk.Button(top, text='Click', style='TButton', command=test_call_back)
but2=tkinter.Button(top, text='Clack', command=test_call_back)
lab=ttk.Label(top, text='Юникод test', style='BW.TLabel')
checkbox=ttk.Checkbutton(top, text='eqweqe')
canv = tkinter.Canvas(top)

but.pack()
but2.pack()
lab.pack()
checkbox.pack()
canv.pack()
top.mainloop()