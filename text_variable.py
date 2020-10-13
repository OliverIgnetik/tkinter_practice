from tkinter import *

w = Tk()

# advantage of text variable
#########################################
# set variable is easier to remember
# easier to modify multiple labels at once

text = StringVar(master=w)

label_1 = Label(w,
                bd=1,
                relief='solid',
                padx=10,
                pady=10,
                font=('Times', 22, 'bold'),
                textvariable=text)
label_1.pack()

label_2 = Label(w,
                bd=1,
                relief='solid',
                padx=10,
                pady=10,
                font=('Times', 22, 'bold'),
                text='hello')
label_2.pack()

text.set('text variable set method')
label_2['text'] = 'label (key, value) pair'

w.mainloop()
