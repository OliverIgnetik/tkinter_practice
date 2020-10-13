import time as tm
import tkinter as tk


w = tk.Tk()
w.title('Current Time')


class clock:
    def __init__(self, master):
        # important attributes
        self.master = master
        self.current_time = tk.StringVar()

        # setup
        self.setup_menu()
        self.setup_clock_display()

        # tick-tock
        self.tick()

    def setup_clock_display(self):
        self.clock_label = tk.Label(
            self.master, font='ariel 45', bg='black', fg='red', textvariable=self.current_time)
        self.clock_label.grid(row=0, column=0)

    def setup_menu(self):
        # menu reference
        self.menu = tk.Menu(self.master)

        # make dropdown
        dropdown = tk.Menu(self.menu, tearoff=0)
        dropdown.add_command(
            label='Small Font', command=lambda: self.clock_label.config(font='ariel 30'))
        dropdown.add_command(
            label='Large Font', command=lambda: self.clock_label.config(font='ariel 50'))
        self.menu.add_cascade(label='font sizes', menu=dropdown)

        # add menu to master
        self.master.config(menu=self.menu)

    def tick(self):
        new_time = tm.strftime('%H:%H:%S')
        self.current_time.set(new_time)
        self.master.after(1000, self.tick)


my_clock = clock(w)

w.mainloop()


# imperative method for writing clock gui
# def display_time():
#     current_time = tm.strftime('%H:%H:%S')
#     clock_label['text'] = current_time
#     w.after(1000, display_time)


# clock_label = tk.Label(w, font='ariel 80', bg='black',
#                        fg='red')
# clock_label.grid(row=0, column=0)

# display_time()
