from tkinter import*
from allfunctions import*
from PIL import ImageTk, Image
import os

picvalue.set("C:/Users/yourname/Desktop/yourfolder/file1.png")
def getimage():
    if os.path.isfile(picvalue.get()):
        image_ = Image.open(picvalue.get())
        n_image = image_.resize((100, 100))
        photo = ImageTk.PhotoImage(n_image)
        return photo
    else:
        print(f"Image file '{picvalue.get()}' not found.")

def changepic(img_label):
    picvalue.set("C:/Users/yourname/Desktop/yourfolder/file2.png")

    photo=getimage()
    img_label.configure(image=photo)
    img_label.photo = photo  # Store a reference to the new PhotoImage

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

        ############# for image
        photo=getimage()
        img_label = Label(window1, image=photo)
        img_label.photo = photo 
        img_label.pack()
        #######################
       
        btn = Button(window1, width=9, height=3, text="openwindow2", command=secondform.secform_wrapper(root, window1, printvalue2, backtomain))
        btn.pack()

        btn2 = Button(window1, width=9, height=3, text="print", command=printvalue)
        btn2.pack()

        btn3 = Button(window1, width=9, height=3, text="exit", command=root.destroy)
        btn3.pack()

        btn4 = Button(window1, width=9, height=3, text="changepic", command=lambda: changepic(img_label))
        btn4.pack()

        root.withdraw()

    firstform()
