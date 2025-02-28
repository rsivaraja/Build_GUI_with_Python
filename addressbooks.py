from tkinter import*
import tkinter.messagebox 
from tkinter.filedialog import*
window=Tk()
window.geometry('800x500')
window.title('Address Book')
address_book={}
def clearall():
    name_entry.delete(0,END)
    address_entry.delete(0,END)
    mobile_entry.delete(0,END)
    email_entry.delete(0,END)
    birthday_entry.delete(0,END)
def add():
    username=name_entry.get()
    if username not in address_book.keys():
        tkinter.messagebox.showinfo('Successful','Successfully saved')
        address_box.insert(END,username)     
    #else:
       # tkinter.messagebox.showinfo('Error','Name already exists')
    address_book[username]=(username,address_entry.get(),mobile_entry.get(),email_entry.get(),birthday_entry.get())
    clearall()
def change_data():
    units=address_box.curselection()
    username=address_box.get(units)
    details=address_book[username]
    #print(details)
    name_entry.insert(0,details[0])
    address_entry.insert(0,details[1])
    mobile_entry.insert(0,details[2])
    email_entry.insert(0,details[3])
    birthday_entry.insert(0,details[4])
def delete_data():
    units=address_box.curselection()
    username=address_box.get(units)
    del address_book[username]
    address_box.delete(units)
    print(address_book)
def save_data():
    file=asksaveasfile(defaultextension='.txt')
    if file:
        print(address_book,file=file)
        tkinter.messagebox.showinfo('Success','File successfully saved')
        address_box.delete(0,END)
        address_book.clear()
    else:
        tkinter.messagebox.showinfo('Error','File not saved')

def open_data():
    global address_book
    address_box.delete(0,END)
    address_book.clear()
    file=askopenfile()
    if file:
        address_book=eval(file.read())
        for name in address_book.keys():
            address_box.insert(END,name)
    else:
        tkinter.messagebox.showinfo('Error','File not selected')



title1=Label(window,text='My Address Book',font=('Lucida Sans Typewriter',12,'normal'))
title1.place(x=150,y=20)
open=Button(window,text='Open',font=('Lucida Sans Typewriter',12,'normal'),command=open_data)
open.place(x=500,y=20)
name=Label(window,text='Name:',font=('Lucida Sans Typewriter',12,'normal'))
name.place(x=500,y=90)
name_entry=Entry(window,font=('Lucida Sans Typewriter',12,'normal'),width=15)
name_entry.place(x=600,y=90)
address=Label(window,text='Address:',font=('Lucida Sans Typewriter',12,'normal'))
address.place(x=500,y=150)
address_entry=Entry(window,font=('Lucida Sans Typewriter',12,'normal'),width=15)
address_entry.place(x=600,y=150)
mobile=Label(window,text='Mobile:',font=('Lucida Sans Typewriter',12,'normal'))
mobile.place(x=500,y=210)
mobile_entry=Entry(window,font=('Lucida Sans Typewriter',12,'normal'),width=15)
mobile_entry.place(x=600,y=210)
email=Label(window,text='Email:',font=('Lucida Sans Typewriter',12,'normal'))
email.place(x=500,y=270)
email_entry=Entry(window,font=('Lucida Sans Typewriter',12,'normal'),width=15)
email_entry.place(x=600,y=270)
birthday=Label(window,text='Birthday:',font=('Lucida Sans Typewriter',12,'normal'))
birthday.place(x=500,y=330)
birthday_entry=Entry(window,font=('Lucida Sans Typewriter',12,'normal'),width=15)
birthday_entry.place(x=600,y=330)
address_box=Listbox(window,width=60,height=20)
address_box.place(x=70,y=50)
edit=Button(window,text='Edit',font=('Lucida Sans Typewriter',12,'normal'),width=5,command=change_data)
edit.place(x=100,y=400)
delete=Button(window,text='Delete',font=('Lucida Sans Typewriter',12,'normal'),width=7,command=delete_data)
delete.place(x=200,y=400)
update=Button(window,text='Update/Add',font=('Lucida Sans Typewriter',12,'normal'),width=11,command=add)
update.place(x=600,y=400)
save=Button(window,text='Save',font=('Lucida Sans Typewriter',12,'normal'),width=40,command=save_data)
save.place(x=170,y=450)

window.mainloop()