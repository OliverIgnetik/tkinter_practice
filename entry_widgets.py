from tkinter import *

w = Tk()
w.geometry('800x800+200+200')

entry_text = StringVar(master=w)
# the use of StringVars are useful for when you have text tied to multiple displays
# generally it allows you to group all the variables in one location but can lead to unreadable code

# define the widgets
label_1 = Label(w,
                bd=1,
                relief='solid',
                height=10,
                width=15,
                font=('Times', 12, 'bold'),
                text='Please enter \nyour name')
label_2 = Label(w,
                bd=1,
                relief='solid',
                height=10,
                width=15,
                font=('Times', 12, 'bold'),
                text='')

entry = Entry(w, textvariable=entry_text, width=15,)

button = Button(width=15, text='click me',
                command=lambda: label_2.config(text=f'hello {entry_text.get()}'))

# organize the widgets
label_1.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=1, column=0)
label_2.grid(row=1, column=1)

w.mainloop()
