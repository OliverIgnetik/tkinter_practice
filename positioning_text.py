from tkinter import *

w = Tk()
# NOTES
################################
# use anchor before justify
# anchor will set the position of the text in the box after padding has been applied
# justify sets the position of the text according to the amount of padding
spacer = Label(w, text='spacer')
spacer.pack()
label = Label(w,
              text="anchor\nanchor anchor",
              bd=1,
              relief='solid',
              font=('Times', 32),
              width=15,
              height=4,
              anchor=SE,
              justify=RIGHT)
label.pack()

spacer = Label(w, text='spacer')
spacer.pack()

label = Label(w,
              text="Justify\nJustify Justify\nJustify Justify Justify",
              bd=1,
              width=15,
              relief='solid',
              font=('Times', 32),
              justify=LEFT)
label.pack()

spacer = Label(w, text='spacer')
spacer.pack()

label = Label(w,
              text="Justify\nJustify Justify\nJustify Justify Justify",
              bd=1,
              width=15,
              relief='solid',
              font=('Times', 32),
              justify=CENTER)
label.pack()

w.configure(width=400, height=800)
w.minsize(400, 250)
w.mainloop()
