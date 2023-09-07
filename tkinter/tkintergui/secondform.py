from tkinter import*
def secform_wrapper(root, parent, printvalue2, backtomain):
    def secform():
        root.deiconify()
        window2 = Toplevel(parent)
        width_value = 500
        height_value = 500

        screen_width = window2.winfo_screenwidth()
        screen_height = window2.winfo_screenheight()

        position_top = int(screen_height / 2 - height_value / 2)
        position_right = int(screen_width / 2 - width_value / 2)

        window2.geometry(f'{width_value}x{height_value}+{position_right}+{position_top}')
        window2.overrideredirect(1)

        btn = Button(window2, width=9, height=3, text="gobacktowindow1", command=backtomain)
        btn.pack()

        btn2 = Button(window2, width=9, height=3, text="print", command=printvalue2)
        btn2.pack()

        root.withdraw()

    return secform
