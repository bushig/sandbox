import tkinter

top = tkinter.Tk()

top.title('харкач')

def test_call_back():
    print('test')
# Code to add widgets will go here...
but=tkinter.Button(top, text='Click', command=test_call_back, relief=tkinter.GROOVE)
lab=tkinter.Label(top, text='Юникод test')
checkbox=tkinter.Checkbutton(top, text='eqweqe')

but.pack()
lab.pack()
checkbox.pack()
top.mainloop()