from tkinter import *

my_window = Tk()

h = my_window.winfo_screenheight()
w = my_window.winfo_screenwidth()

my_window.geometry('{w:d}x{h:d}+0+0'.format(w=w, h=h))

my_window.mainloop()
