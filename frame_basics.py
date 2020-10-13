from tkinter import *

# frames are used for organizing a complex gui

w = Tk()

# OOP way of making frames


class input_widget(Frame):
    def __init__(self, labels, location, master=None):
        # checks on inputs
        if len(labels) != 3:
            raise ValueError('invalid number of labels')
        if len(location) != 2:
            raise ValueError('Need to input a row and column value')
        row, column = location

        # super related constructor code
        super().__init__(master)
        self.master = master
        self.id = id(self)
        self.grid(row=row, column=column)
        super().config(padx=20, pady=20)

        # store widgets
        self.labels_container = []
        self.buttons_container = []
        self.entries_container = []

        # set up layout
        self.layout(labels)

    def layout(self, labels):
        i = 0
        for label in labels:
            label = Label(self, text=f'{label}')
            label.grid(column=0, row=i)
            self.labels_container.append(label)
            i += 1

        j = 0
        for j in range(len(labels)):
            entry = Entry(self)
            entry.grid(column=1, row=j)
            self.entries_container.append(entry)
            j += 1

        button_submit = Button(self, text='Submit')
        button_submit.grid(row=3, columnspan=2)
        self.buttons_container.append(button_submit)


name_frame = input_widget(
    labels=['first name', 'middle name', 'last name'], location=(0, 0), master=w)
address_frame = input_widget(
    labels=['First Line', 'Town', 'Country'], location=(0, 1), master=w)
hobbies_frame = input_widget(
    labels=['food', 'sport', 'hobbies'], location=(1, 0), master=w)
results_frame = input_widget(
    labels=['failures', 'achievements', 'awards'], location=(1, 1), master=w)

print('name frame labels')
for label in name_frame.labels_container:
    print(label['text'])

print('\ncheck of ids')
print(
    f'object attribute : {address_frame.id}\nid operator {id(address_frame)}')
w.mainloop()

print(help(input))

# imperative way
# frame_name = Frame(w)

# label_first = Label(frame_name, text='first name')
# label_first.grid(column=0, row=0)
# label_middle = Label(frame_name, text='middle name')
# label_middle.grid(column=0, row=1)
# label_last = Label(frame_name, text='last name')
# label_last.grid(column=0, row=2)

# entry_first = Entry(frame_name)
# entry_first.grid(column=1, row=0)
# entry_middle = Entry(frame_name)
# entry_middle.grid(column=1, row=1)
# entry_last = Entry(frame_name)
# entry_last.grid(column=1, row=2)

# button_submit = Button(frame_name, text='Submit')
# button_submit.grid(row=3, columnspan=2)

# frame_name.grid(row=0, column=0)
