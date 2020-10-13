from random import randint
from tkinter import Button, Canvas, StringVar, Frame, Label, Tk


class paint_click_app(Canvas):
    def __init__(self, master, width, height, bg, pos):
        super().__init__(master=master, width=width, height=height, bg=bg)

        # bind buttons
        self.bind('<Button-1>', self.random_line)
        self.bind('<Button-3>', self.delete_lines)

        # get row and column and position this app
        row, column = pos
        self.grid(column=column, row=row)

    def random_line(self, event):
        x1 = randint(0, 400)
        y1 = randint(0, 400)
        x2 = randint(0, 400)
        y2 = randint(0, 400)
        self.create_line(
            x1, y1, x2, y2, fill=f'#{randint(0,0xffffff):06x}', width=20)

    def delete_lines(self, event):
        self.delete('all')


class draw_line_app(Canvas):
    def __init__(self, master, width, height, bg, pos):
        super().__init__(master=master, width=width, height=height, bg=bg)
        self.bind('<Button-1>', self.draw_line)
        self.bind('<Button-3>', self.delete_lines)

        self.clicks = 0
        self.p1 = [0, 0]
        self.p2 = [0, 0]

        # position this app
        row, column = pos
        self.grid(column=column, row=row)

    def draw_line(self, event):
        if (self.clicks == 0):
            self.p1[0] = event.x
            self.p1[1] = event.y
            self.clicks = 1
        else:
            self.p2[0] = event.x
            self.p2[1] = event.y
            self.create_line(
                self.p1[0], self.p1[1], self.p2[0], self.p2[1], fill='black', width=10)
            self.clicks = 0

    def delete_lines(self, event):
        self.delete('all')


class coordinate_click_app(Frame):
    def __init__(self, master, width, height, pos):
        super().__init__(master=master, width=width, height=height)

        # variables
        self.coordinates = StringVar()

        # set up the canvas
        self.canvas = Canvas(master=self, width=width,
                             height=int(height/3))
        self.canvas.grid(column=0, row=1)

        # set up the label
        self.label = Label(
            self, textvariable=self.coordinates, height=1, width=30, bd=1)
        self.label.grid(column=0, row=2)

        # bind the button
        self.canvas.bind('<Button-1>', self.onclick)

        # position this app
        row, column = pos
        self.grid(column=column, row=row)

    def onclick(self, event):
        self.coordinates.set(f'x={event.x}, y={event.y}')


w = Tk()

Label(w, text='Coordinate Click app').grid(row=0, column=0)
app1 = coordinate_click_app(w, 400, 400, pos=(1, 0))

Label(w, text='Paint Click app').grid(row=0, column=1)
app2 = paint_click_app(w, 400, 400, bg='white', pos=(1, 1))

Label(w, text='Draw line app').grid(row=0, column=2)
app3 = draw_line_app(w, 400, 400, bg='white', pos=(1, 2))

w.mainloop()
