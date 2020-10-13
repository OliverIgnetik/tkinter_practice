from tkinter import *

# also includes an aside on focus and tab order
# tab order depends on the order of object instantiation
# NOT THE POSITION!

w = Tk()

ftemp_input = StringVar(master=w)
ctemp_output = StringVar(master=w)


def convert():
    value = ftemp_input.get()
    if value == '':
        return
    res = 5/9*(float(value)-32)
    ctemp_output.set(f'{round(res,2)} degrees C')


label_1 = Label(w, text='Enter Fahrenheit')
label_2 = Label(w, text='Celsius Temperature')
label_3 = Label(w, textvariable=ctemp_output)

entry = Entry(w, textvariable=ftemp_input)

button = Button(width=15, text='click me',
                command=convert)

# organize the widgets
label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)
label_3.grid(row=1, column=1)
entry.grid(row=0, column=1)
button.grid(row=2, column=0)

entry.focus()

w.mainloop()
