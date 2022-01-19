from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox
import tkinter as tk


root = Tk()
root.title("Virtual Keyboard")
root.geometry('1200x800')

class Keypad(tk.Frame):

    cells = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.target = None
        self.memory = ''

        for y, row in enumerate(self.cells):
            for x, item in enumerate(row):
                b = tk.Button(self, text=item, command=lambda text=item:self.append(text),font=("Arial", 14), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
                b.grid(row=y, column=x, sticky='news')

        x = tk.Button(self, text='Space', command=self.space,font=("Arial", 14), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
        x.grid(row=0, column=10, columnspan='4', sticky='news')

        x = tk.Button(self, text='tab', command=self.tab,font=("Arial", 14), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
        x.grid(row=0, column=14, columnspan='3', sticky='news')

        x = tk.Button(self, text='Backspace', command=self.backspace,font=("Arial", 14), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
        x.grid(row=0, column=17,columnspan='3', sticky='news')

        x = tk.Button(self, text='Clear', command=self.clear,font=("Arial", 14), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
        x.grid(row=0, column=20, columnspan='3',  sticky='news')

        x = tk.Button(self, text='Hide', command=self.hide,font=("Arial", 14), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
        x.grid(row=0, column=23, columnspan='3', sticky='news')


    def get(self):
        if self.target:
            return self.target.get("1.0", "end-1c")

    def append(self, text):
        if self.target:
            self.target.insert('end', text)

    def clear(self):
        if self.target:
            self.append("Clear")

    def backspace(self):
        if self.target:
            self.append("BackSpace")

    def space(self):
        if self.target:
            self.append("Space")

    def tab(self): # 5 spaces
        self.append("tab")

    def copy(self):
        if self.target:
            self.memory = self.get()
            self.label['text'] = 'memory: ' + self.memory
            print(self.memory)

    def paste(self):
        if self.target:
            self.append(self.memory)

    def show(self, entry):
        self.target = entry

        self.place(relx=0.5, rely=0.5, anchor='c')

    def hide(self):
        self.append("hide")

#-------------------------------------------------------

def print_output():
    mbox.showinfo("Text Entered", "Text Entered :\n\n" + text_enter.get('1.0',END))

def des_f1():
    f1.destroy()


f1 = Frame(root, height=700, width=1000)
f1.propagate(0)
f1.pack(side='top')



c = Canvas(f1, width=1000, height=700)
c.pack()
p1 = PhotoImage(file='Images/keyboard.gif')
c.create_image(200, 100, image=p1, anchor=NW)

start1 = Label(f1, text='VIRTUAL KEYBOARD', font=("Arial", 50), fg="magenta", underline = 0)
start1.place(x=150, y=10)

startb = Button(f1, text="START",command=des_f1,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 180 , y =550 )
f1.destroy()

f2 = Frame(root, height=700, width=1000)
f2.propagate(0)
f2.pack(side='top')

keypad = Keypad(root)

#task
start2 = Label(f2, text='Enter your Name', font=("Arial", 40), fg="black")
start2.place(relx= 0.5, rely=0.4, anchor=CENTER)

#credits
start2 = Label(f2, text='forked from akash435/Virtual-Keyboard', font=("Arial", 40), fg="black")
start2.place(relx= 0.5, rely=0.8, anchor=CENTER)

#text in text field
text_enter = tk.Text(f2, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_enter.place(x=50, y=10)

keypad.show(text_enter)

def exit_win():
    root.destroy()

#exit button
exitb = Button(root, text="give up",command=exit_win,font=("Arial", 30), bg = "red", fg = "black", borderwidth=3, relief="raised")
exitb.place(relx =0.5 , rely =0.8 , anchor=CENTER)


root.protocol("WM_DELETE_WINDOW", exit_win)
root.mainloop()
