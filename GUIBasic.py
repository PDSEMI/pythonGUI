from tkinter import *
from tkinter import messagebox, colorchooser, filedialog
import sys

#function setup
def mHello():
	Label(text = "Hello").pack()
def Hello(event):
	messagebox.showinfo(title='Show Information', message ='Hello User')
	'''
	messagebox.method
	showinfo	:	show information
	showwarning	:	show alert
	show error	:	show error
	askquestion	:	ask question, yes-no question
	askokcancel :	ask question, ok-cancel question
	'''
def Exit(event):
	status = messagebox.askyesno(title="confirmation", message="do yo want to exit program?")
	if status > 0:
		sys.exit()
def fColor(event):
	#Color dialog
	colorchooser.askcolor()
	Label(text="")
def fOpen(event):
	filedialog.askopenfile()

#init the GUI
gui = Tk()


#GUI setup
gui.geometry("700x700") #set the size of canvas
gui.title("GUI Basic") #Title of GUI


#GUI attribute
'''
Label 	: 	unchanged attrib/object
Button 	:	clickable attrib/object
			can trigger event
Entry	:	editable textbox
Menu 	:	Menu bar
Radio 	:	choose
SpinBox : 	vary value
ListBox :	box with listed option
'''
mlabel = Label(text="PDSEMI", fg="white", bg ="black") #create Label
mlabel.pack() #put in canvas 

mButton = Button(text="SUBMIT",fg="red",bg="pink", command=mHello) #create Buttom
mButton.pack()
b1 = Button(text = "Hello")
b1.bind('<Button-1>', Hello) # bind button with event and funtion
b1.pack()
exitButton = Button(text='EXIT')
exitButton.bind('<Button-1>', Exit)
exitButton.pack()
b2 = Button(text='Color')
b2.bind('<Button-1>', fColor)
b2.pack()
b3 = Button(text="Select File:")
b3.bind('<Button-1>', fOpen)
b3.pack()

mEntry = Entry() #crete EntryBox
mEntry.pack()

mMenubar = Menu(gui) #create Menubar
#create subMenu
fileMenu = Menu(mMenubar, tearoff = 0) 
helpMenu = Menu(mMenubar, tearoff = 0)
'''
tearoff : movable menu,  
'''
fileMenu.add_command(label="New") #create subMenu command
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save...As")
helpMenu.add_command(label="Help")

mMenubar.add_cascade(label ="File", menu = fileMenu) #link menubar with menu
mMenubar.add_cascade(label ="Help", menu = helpMenu)

gui.config(menu = mMenubar) #add menu to canvas , the last thing to do

#Radio Button
r1 = Radiobutton(text='Male',value=1)
r2 = Radiobutton(text = 'Female',value=2)
r1.pack()
r2.pack()

#SpinBox
spin1 = Spinbox(from_=0,to=10)
spin1.pack();

#ListBox
l1 = Listbox()
l1.insert(1,"Python")
l1.insert(2,"Java")
l1.insert(3,"Datbase")
l1.pack();

#Slider
sl1=Scale(orient = HORIZONTAL,width=20,from_=10,to=50,tick=10,length=500)
sl1.pack()


#Displaying
gui.mainloop()  

