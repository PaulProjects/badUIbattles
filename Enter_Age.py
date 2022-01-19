from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox
import tkinter as tk

root = Tk()
root.title("Virtual Keyboard")
root.geometry('1200x800')

# variable is stored in the root object
root.counter = 0

def clicked():
    root.counter += 1
    L2['text'] = 'Age: ' + str(root.counter)
    messagebox.showinfo("Buy Premium to remove this reminder","Added 1 to the counter")

def popup():
    messagebox.showinfo("WARNING WARNING", "Wrong age detected. Please enter the age in days")


L1 = Label(root, text="Enter your Age")
L1.pack()

b = Button(root, text="Next", command=popup)
b.pack()

L2 = Label(root, text="Age: Invalid")
L2.pack()

//The add

photo = PhotoImage(file = r"Images/keyboard.gif")
c= Button(root, text = 'Click Me !', image = photo)
c.pack(side = TOP)



def exit_win():
    clicked()

root.protocol("WM_DELETE_WINDOW", exit_win)
root.mainloop()