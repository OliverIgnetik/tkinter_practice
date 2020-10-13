from tkinter import *
width, height = 1280, 720
x, y = 100, 50

w = Tk()
w.title('setting window size')

# OPTION 1
######################################
# w.configure(width=width, height=height)

# OPTION 2 - PREFERRED
######################################
g = f'{width}x{height}+{x}+{y}'
w.geometry(g)

# FIXING SIZE, MIN SIZE - definitely want to consider doing this
######################################
# w.resizable(width=False, height=True)
w.minsize(width, height)

w.mainloop()
