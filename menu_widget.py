import tkinter as tk


class app:
    def __init__(self, master, labels):
        self.master = master
        self.text = tk.StringVar()
        self.label = tk.Label(master=self.master, textvariable=self.text)
        self.label.pack()
        self.construct_menu(labels)

    def construct_menu(self, labels):
        self.menu = tk.Menu(self.master)
        for label in labels:
            if label == 'quit':
                self.menu.add_command(label=label, command=self.quit)
            elif label == 'info':
                self.menu.add_command(label=label, command=self.info_display)
            else:
                self.menu.add_command(label=label)

        # set up drop down menu
        drop_down = tk.Menu(self.menu, tearoff=1)
        drop_down.add_command(label='red')
        drop_down.add_command(label='blue')
        drop_down.add_separator()
        drop_down.add_command(label='green')

        self.menu.add_cascade(label='colour', menu=drop_down)
        self.master.config(menu=self.menu)

    def quit(self):
        self.master.destroy()

    def info_display(self):
        self.text.set('Here is the secret info')


w = tk.Tk()

app = app(w, ['file', 'info', 'quit'])

w.mainloop()
