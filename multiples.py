from tkinter import*
from tkinter.ttk import*
window=Tk()
#window.geometry('300x200')
window.title('Multiplication')
def maths():
    m1=choice.get()
    m2=endval1.get()
    text=''
    for i in range(1,m2+1):
        text+=f'{m1}x{i}={m1*i}\n'
    table.config(text=text)    
heading=Label(window, text='Multiplication table',font=('Lucida Sans Typewriter',11,'normal'))
heading.place(x=10,y=25)
nr=Label(window,text='Number and Range:',font=('Lucida Sans Typewriter',9,'normal'))
nr.place(x=6,y=60)
choice=IntVar()
numbers=Combobox(window,textvariable=choice,width=3)
numbers['values']=(1,2,3,4,5,6,7,8,9)
numbers.place(x=130,y=60)
endval1=IntVar()
r1=Radiobutton(window,text='10',variable=endval1,value=10)
r2=Radiobutton(window,text='20',variable=endval1,value=20)
r3=Radiobutton(window,text='30',variable=endval1,value=30)
r1.place(x=190,y=60)
r2.place(x=190,y=80)
r3.place(x=190,y=100)
table=Label(window,text='',font=('Lucida Sans Typewriter',9,'normal'))
table.place(x=130,y=120)
gen=Button(window,text='Generate',command=maths)
gen.place(x=60,y=100)
window.mainloop()
