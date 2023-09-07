from tkinter import*
from allfunctions import*

def firstform_wrapper(root, secondform, backtomain):
    def firstform():
        root.deiconify()
        window1 = Toplevel(root)
        width_value = 500
        height_value = 500

        screen_width = window1.winfo_screenwidth()
        screen_height = window1.winfo_screenheight()

        position_top = int(screen_height / 2 - height_value / 2)
        position_right = int(screen_width / 2 - width_value / 2)

        window1.geometry(f'{width_value}x{height_value}+{position_right}+{position_top}')
        window1.overrideredirect(1)

        btn = Button(window1, width=9, height=3, text="openwindow2", command=secondform.secform_wrapper(root, window1, printvalue2, backtomain))
        btn.pack()

        btn2 = Button(window1, width=9, height=3, text="print", command=printvalue)
        btn2.pack()

        btn3 = Button(window1, width=9, height=3, text="exit", command=root.destroy)
        btn3.pack()

        root.withdraw()

    firstform()