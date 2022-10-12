from tkinter import *

window = Tk()

bg = window.background.color()
bg = ("blue")

def convert():
    print("Success")
    grams=float(e1Value.get())*1000
    pounds=float(e1Value.get())*2.20462
    ounces=float(e1Value.get())*35.274

    t1.delete ("1.0", END)
    t1.insert(END, grams)

    t2.delete ("1.0", END)
    t2.insert(END, pounds)

    t3.delete ("1.0", END)
    t3.insert(END, ounces)

b1=Button(window, text="convert", command=convert, bg="green", fg="blue")
b1.grid(column=1, row=0)


e1Value=StringVar()

e1 = Entry(window, textvariable=e1Value)
e1.grid(column=1, row=2)

t1=Text(window, height=1, width=20)
t1.grid(column=0, row=3)

t2=Text(window, height=1, width=20)
t2.grid(column=1, row=3)

t3=Text(window, height=1, width=20)
t3.grid(column=2, row=3)




window.mainloop()
