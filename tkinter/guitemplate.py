from tkinter import*

root=Tk()
value1=StringVar()
value1.set("value")

def printvalue():
	print(value1.get())
def printvalue2():
	value1.set("value2")
	print(value1.get())

def backtomain():
	firstform()
	
def secform():
	root.deiconify()
	window2=Toplevel(root)
	width_value=500
	height_value=500

	screen_width = window2.winfo_screenwidth()
	screen_height = window2.winfo_screenheight()

	position_top = int(screen_height/2 - height_value/2)
	position_right = int(screen_width / 2 - width_value/2)

	window2.geometry(f'{width_value}x{height_value}+{position_right}+{position_top}')
	window2.overrideredirect(1)

	btn=Button(window2,width=9,height=3,text="gobacktowindow1",command=backtomain)
	btn.pack()

	btn2=Button(window2,width=9,height=3,text="print",command=printvalue2)
	btn2.pack()

	root.withdraw()

def firstform():
	root.deiconify()
	window1=Toplevel(root)
	width_value=500
	height_value=500

	screen_width = window1.winfo_screenwidth()
	screen_height = window1.winfo_screenheight()

	position_top = int(screen_height/2 - height_value/2)
	position_right = int(screen_width / 2 - width_value/2)

	window1.geometry(f'{width_value}x{height_value}+{position_right}+{position_top}')
	window1.overrideredirect(1)

	btn=Button(window1,width=9,height=3,text="openwindow2",command=secform)
	btn.pack()

	btn2=Button(window1,width=9,height=3,text="print",command=printvalue)
	btn2.pack()

	btn3=Button(window1,width=9,height=3,text="exit",command=root.destroy)
	btn3.pack()
	root.withdraw()
	
firstform()
root.attributes('-alpha', 0)
root.withdraw()
root.mainloop()
