from tkinter import *

w = Tk()
w.geometry('200x100+200+200')

clicks = 0


def on_click():
    global clicks
    clicks += 1
    if (clicks % 2 == 0):
        text.set('click the button')
    else:
        text.set('button clicked')


text = StringVar(master=w)
text.set('click the button')

button1 = Button(w, text='click me', command=on_click)
button1.pack()
button1.clicks = 0

label_1 = Label(w,
                bd=1,
                relief='solid',
                padx=10,
                pady=10,
                height=10,
                width=15,
                font=('Times', 12, 'bold'),
                textvariable=text)
label_1.pack()


w.mainloop()
