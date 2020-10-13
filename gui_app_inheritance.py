from tkinter import *

w = Tk()

# OOP way of making frames

# this clearly shows the advantage of using Tkinter variables


class app_frame(Frame):
    def __init__(self, master=None):
        # super related constructor code
        super().__init__(master)
        self.users_name = StringVar()
        self.users_name.set('John Doe')
        self.display_string = StringVar()
        self.display_output()

        # you don't need to call super anymore
        self.grid(row=0, column=0)
        super().config(padx=20, pady=20)

        # widget storage
        self.widgets = []
        # set up layout
        self.layout()

    def layout(self):
        entry_label = Label(self, name='entry_label', text='enter your name')
        entry_label.grid(column=0, row=0)
        self.widgets.append(entry_label)

        display_label = Label(
            self, textvariable=self.display_string, relief='solid', name='display_label')
        display_label.grid(column=1, row=1)
        self.widgets.append(display_label)

        entry = Entry(self, textvariable=self.users_name, name='entry')
        entry.grid(column=1, row=0)
        self.widgets.append(Entry)

        button = Button(self, text='click me',
                        command=self.display_output, name='button')
        button.grid(column=0, row=1)
        self.widgets.append(button)

    def display_output(self):
        self.display_string.set('Hello ' + self.users_name.get())


app = app_frame(master=w)

w.mainloop()
