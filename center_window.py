from tkinter import *


def center_size(w, hw, ww):

    sh = w.winfo_screenheight()
    sw = w.winfo_screenwidth()

    x = sw/2 - ww/2
    y = sh/2 - hw/2

    x, y = int(x), int(y)

    g = f'{ww}x{hw}+{x}+{y}'
    w.geometry(g)


w = Tk()
w.title('centering the window on the screen')

center_size(w, 800, 800)

w.mainloop()
