from tkinter import *

w = Tk()

label = Label(w,
              bd=8,
              relief='solid',
              font=('Times', 22, 'bold'),
              bg='red',
              fg='white',
              text=f'hello')

label.pack()

for key in label.keys():
    print(f'{key} : {label[key]}')

w.mainloop()
