from tkinter import *

w = Tk()

colours = ['red', 'yellow', 'green']

for j in range(len(colours)):
    c = Canvas(w, width=200, height=200, bg=colours[j])
    if j != 1:
        c.create_line(0, 0, 200, 200, fill='black', width=5)
        c.create_line(0, 200, 200, 0, fill='black', width=5)
        c.create_line(0, 100, 200, 100, fill='black', width=5,
                      arrow='both', arrowshape=(60, 30, 14))
        c.create_line(100, 0, 100, 200, fill='black', width=5,
                      arrow='both', arrowshape=(60, 30, 14))

    else:
        c.create_oval(5, 5, 195, 195, fill='white')

    c.grid(column=j, row=0, padx=5)

w.mainloop()
