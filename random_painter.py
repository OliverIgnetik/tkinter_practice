from random import *
from tkinter import *


def random_colour_code():
    hex_chars = ['0', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    colour_code = '#'
    for _ in range(0, 6):
        colour_code += choice(hex_chars)
    return colour_code


def random_colour_code_lean():
    #:06x tells the f-string that we need a hex number with 6 elements
    return f'#{randint(0,0xffffff):06x}'


w = Tk()
dim = 800
c = Canvas(w, width=800, height=800, bg='white')
c.grid(column=0, row=0)

for _ in range(500):
    x1 = randint(0, dim)
    x2 = randint(0, dim)
    y1 = randint(0, dim)
    y2 = randint(0, dim)

    rand_width = randint(1, 10)

    c.create_line(x1, y1, x2, y2, fill=random_colour_code_lean(),
                  width=rand_width)
    # updates the canvas at each loop iteration
    c.update()

w.mainloop()
