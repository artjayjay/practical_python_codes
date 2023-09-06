from tkinter import*
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os.path
from os import path
import tkinter.messagebox
import sqlite3 as db
import os
'''
                                   when converting to exe please dont 
                                   forget to replace .py extension to exe extension
'''
def dataentry():#==============edit to exe==========
	os.system('mysystemfinal2.exe')

def donothing():
    pass

def about():#=============================== data entry ======================================
	top=Toplevel()
	top.title("About")
	top.geometry("792x400")
	top.iconbitmap("Normal Balance.ico")
	x=Label(top,image=logo).pack()
	button3.config(state="disabled")
	top.protocol('WM_DELETE_WINDOW',donothing)
	topbtn=Button(top,text="  CLOSE",bg="white",font=("Arial" ,10),command=lambda:enble(top),padx=10,pady=7)
	topbtn.place(x=370,y=330)
def enble(top):
	button3.config(state="active")
	top.destroy()

#============================admin details===================
def admindetails():
	conn=db.connect('account.db')
	cur=conn.cursor()
	cur.execute("SELECT lastname, firstname FROM admin")#==========tignan mo====
	rows=cur.fetchall()
	for row in rows:
		last=row[0]
		first=row[1]
		conn.close()
	name=(first+" "+last)
	if first=="" or last=="":
			name=("firstname"+" "+"lastname")
	return name

def  edit():
	os.system('editprofile.exe')#========== edit profile form

def logout():
	root.destroy()
	os.system('loginform2.exe')#=========== logout form ==========

root=Tk()
root.title("Normal Balance System")
width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()
root.geometry("%dx%d+-8+0" % (width_value, height_value))
root.iconbitmap("Normal Balance.ico")

logo = PhotoImage(file="about.png")
#================================== configure the background image ==============================
my_pic=Image.open("bgkoedited.png")
resized=my_pic.resize((width_value,height_value+100),Image.ANTIALIAS)
#================================== display background image ====================================
backgroundpic=ImageTk.PhotoImage(resized)
lbllogo=Label(root,image=backgroundpic,bg="#A8A7A7")
lbllogo.pack()
#=================================== display frame for buttons =================================
topframe=Frame(root,padx=10,bd=2,relief=RIDGE,bg="#f070a9")
topframe.place(x=0,y=0)
#================================== configure logo =============================================
my_pic1=Image.open("knowledgeville_nobackground.png")
resized1=my_pic1.resize((210,160),Image.ANTIALIAS)

mainlogo=ImageTk.PhotoImage(resized1)
#================================== display Title =============================================
maintitle=ImageTk.PhotoImage(file="titlenormal.png")
lbltitle=Label(root,image=maintitle,bg="white")
lbltitle.place(x=width_value-680,y=height_value-800)
lb=Label(topframe,text="\n",font="Arial 10 bold",bg="#f070a9")
lb.pack()
button=Button(topframe,text="  CLOSE",bg="white",font=("Arial" ,14),command=root.destroy,padx=78,pady=7)
button.pack()
lbl1=Label(topframe,text="\n",font="Arial 10 bold",bg="#f070a9")
lbl1.pack()
button2=Button(topframe,text="  LOGOUT",bg="white",font=("Arial" ,14),command=logout,padx=68,pady=7)
button2.pack()
lbl2=Label(topframe,text="\n",font="Arial 10 bold",bg="#f070a9")
lbl2.pack()
button3=Button(topframe,text="ABOUT",bg="white",font=("Arial" ,14),command=about,padx=81,pady=7)
button3.pack()
lbl3=Label(topframe,text="\n",font="Arial 10 bold",bg="#f070a9")
lbl3.pack()
button4=Button(topframe,text="DATA ENTRY",bg="white",font=("Arial" ,14),command=dataentry,padx=52,pady=7)
button4.pack()
lbl4=Label(topframe,text="\n\n\n\n",font="Arial 25 bold",bg="#f070a9")
lbl4.pack()
lbllogo=Label(topframe,image=mainlogo,bg="#f070a9")
lbllogo.pack()
lbl5=Label(topframe,text="\n",font="Arial 25 bold",bg="#f070a9")
lbl5.pack()
button5=Button(root,fg="#363636",text="EDIT PROFILE",bg="white",font=("Arial" ,14),padx=14,command=edit)
button5.place(x=width_value-575,y=height_value-220)

name=admindetails()
lblName=Label(root,fg="#363636",text=name,font=("times new roman" ,25, "bold"),bg="white")
lblName.place(x=width_value-599,y=height_value-310)

def callback():
	conn=db.connect('account.db')
	cur=conn.cursor()
	cur.execute("SELECT picture FROM admin")#==========tignan mo====
	rows=cur.fetchone()
	p=""
	p=rows[0]
	conn.close()

	if path.exists(p)==True:
		print("Your File Exist!")
	else:
		print("No file found in this directory "+p)
		p="profile.png"
		tkinter.messagebox.showinfo("No directory","Your path does not exist please try another one")
	my_pic=Image.open(p)
	img1=my_pic.resize((320,320),Image.ANTIALIAS)
	img=ImageTk.PhotoImage(img1)
	
	return img

def refresh():
	root.destroy()
	os.system('mainform.exe')

button6=Button(root,fg="#363636",text="REFRESH",bg="white",font=("Arial" ,14),padx=14,command=refresh)
button6.place(x=width_value-555,y=height_value-160)
img=callback()
panel=Label(root, image=img)
panel.place(x=width_value-655,y=height_value-670)

root.mainloop()
