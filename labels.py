from tkinter import *

w = Tk()


def center_size(w, hw, ww):

    sh = w.winfo_screenheight()
    sw = w.winfo_screenwidth()

    x = sw/2 - ww/2
    y = sh/2 - hw/2

    x, y = int(x), int(y)

    g = f'{ww}x{hw}+{x}+{y}'
    w.geometry(g)


center_size(w, 600, 800)


# SET LABEL PARAMETERS
######################################
# Note:
# 1. width is defined in text units
# 2. set font using tuple
# 3. height is defined in units of font size lines. This means pady and height stack
# 4. pady is more suitable when you want consistent spacing irregardless of font size
label_1 = Label(w, text="height is relative to line height", bg='green',
                fg='white', font='Times 10', width=50, borderwidth=5, relief='solid', height=4)
label_2 = Label(w, text="width is relative to text units", bg='blue',
                fg='white', font='Broadway 12', pady=30, width=40, bd=1, relief='sunken')
label_3 = Label(w, text="multiple\nlines", bg='pink',
                fg='white', font=('Times', 34, 'bold', 'italic'), pady=10, width=30)
label_4 = Label(w, text="anchor", bd=1, relief='solid', font=(
    'Times', 12, 'italic'), width=80, height=10, anchor='ne')
label_5 = Label(w, text="padx and pady", bd=1, relief='solid', font=(
    'Times', 12, 'italic'), padx=150, pady=20)

label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
label_5.pack()

w.mainloop()
