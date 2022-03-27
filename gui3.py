from tkinter import *

loop = Tk()
loop.title("Learning")
loop.geometry('400x300')
f1 = Frame(loop, bg='Pink', borderwidth=7, relief=SUNKEN)
f1.pack(side=BOTTOM, anchor='se', fill='y')
f2 = Frame(loop, bg='Black',borderwidth=10,relief=SUNKEN)
f2.pack(side=TOP, anchor='nw', fill="x")

text = Label(f1, text="Program gui window",bg='Orange',fg="Black")
text.pack(pady=142)

text1 = Label(f2, text="Program gui window", bg='Green', fg="Purple")
text1.pack(pady=142)

loop.mainloop()