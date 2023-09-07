from tkinter import *

import firstform
import secondform

root = Tk()

def backtomain():
    initform()

def initform():
    firstform.firstform_wrapper(root, secondform, backtomain)

initform()
root.attributes('-alpha', 0)
root.withdraw()
root.mainloop()
