from tkinter import *
from tkinter import messagebox, colorchooser, filedialog
import sys

#init the GUI
gui = Tk()


#GUI setup
gui.geometry("700x700") #set the size of canvas
gui.title("GUI Basic") #Title of GUI


#GUI attribute
'''
using grid we don't need to pack!!!
'''
l1 = Label(text = "Username:")
l2 = Label(text = "password")
e1 = Entry()
e2 = Entry()
l1.grid(row = 0)
l2.grid(row = 1)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)



#Displaying
gui.mainloop()  

