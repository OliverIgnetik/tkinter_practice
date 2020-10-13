from tkinter import *


class Cfrm(Frame):

    def createWidgets(self):

        self.text = Text(self, width=50, height=10)
        self.text.insert('1.0', 'some text will be here')
        self.text.tag_configure('big', font=('Verdana', 24, 'bold'))

        self.text["state"] = "disabled"
        self.text.grid(row=0, column=1)

        self.quitw = Button(self)
        self.quitw["text"] = "exit",
        self.quitw["command"] = self.quit
        self.quitw.grid(row=1, column=1)

    def __init__(self, master=None):
        # best way to call init
        super().__init__(master)
        # Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


w = Tk()

frame_instance = Cfrm(w)

frame_instance.mainloop()
