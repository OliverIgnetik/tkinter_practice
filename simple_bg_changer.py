from tkinter import *

w = Tk()

label = Label(w,
              bd=1,
              relief='solid',
              padx=10,
              pady=10,
              height=10,
              width=15,
              bg='white')

button1 = Button(text='red',
                 command=lambda: label.config(bg='red'))
button2 = Button(text='black',
                 command=lambda: label.config(bg='black'))
button3 = Button(text='green',
                 command=lambda: label.config(bg='green'))

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
label.grid(row=1, columnspan=3)

w.mainloop()
