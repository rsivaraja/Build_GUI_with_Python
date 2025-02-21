from tkinter import*
import tkinter.messagebox 
import random

window=Tk()
user=Entry(window,font=('Lucida Sans Typewriter',20,'normal'),width=5)
user.place(x=50,y=10)
num2=random.randint(1,100)

def check():
    global num2 
    num1=int(user.get())
    if num1>num2:
        tkinter.messagebox.showinfo('high','Your guess is too high.')
    elif num1==num2:
        tkinter.messagebox.showinfo('CORRECT')
    else:
        tkinter.messagebox.showinfo('low','Your guess is too low.')
check=Button(window,text='Enter',font=('System','16','normal'),command=check)
check.place(x=110,y=50)
window.mainloop()
