from tkinter import *
from tkinter import messagebox, colorchooser, filedialog
import sys

#init the GUI
gui = Tk()


#GUI setup
gui.geometry("700x700") #set the size of canvas
gui.title("GUI Basic") #Title of GUI


#GUI attributr
l1 = Label(text = "Username:")
l1.pack(side=LEFT) #set the position with .pack()
e1 = Entry(bd = 5) #bd: border
e1.pack(side=RIGHT)

'''
side : LEFT, RIGHT, TOP
'''
#Displaying
gui.mainloop()  

