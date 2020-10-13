from tkinter import *

w = Tk()
w.geometry('800x800+200+200')

text = StringVar(master=w)
text.set('some boxes')

label_1 = Label(w,
                bd=1,
                relief='solid',
                padx=10,
                pady=10,
                height=10,
                width=15,
                font=('Times', 12, 'bold'),
                textvariable=text)
label_2 = Label(w,
                bd=1,
                relief='solid',
                padx=10,
                pady=10,
                height=10,
                width=15,
                font=('Times', 12, 'bold'),
                textvariable=text)

label_3 = Label(w,
                bd=1,
                relief='solid',
                padx=10,
                pady=10,
                height=10,
                width=15,
                font=('Times', 12, 'bold'),
                textvariable=text)

button = Button(width=50, text='click me',
                command=lambda: text.set('we got clicked'))

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=0, column=2)
button.grid(row=1, columnspan=3)

w.mainloop()
