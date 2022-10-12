from tkinter import *

window = Tk()

def convert():
    print("KM Success")
    miles=float(e1Value.get())*1.6

    t1.delete ("1.0", END)
    t1.insert(END, miles)

b1=Button(window, text="convert", command=convert, bg="green", fg="blue")
b1.grid(column=0, row=0)


e1Value=StringVar()

e1 = Entry(window, textvariable=e1Value)
e1.grid(column=0, row=2)

t1=Text(window, height=1, width=20)
t1.grid(column=0, row=3)



window.mainloop()
