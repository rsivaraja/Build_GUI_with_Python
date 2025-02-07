from tkinter import*
import tkinter.messagebox 
import time
window=Tk()
window.title('Stopwatch')
window.geometry('260x100')


h=StringVar()
h.set('00')
hours=Entry(window,font=('Lucida Sans Typewriter',20,'normal'),width=2,textvariable=h)
hours.place(x=40,y=20)
m=StringVar()
m.set('00')
minutes=Entry(window,font=('Lucida Sans Typewriter',20,'normal'),width=2,textvariable=m)
minutes.place(x=90,y=20)
s=StringVar()
s.set('00')
seconds=Entry(window,font=('Lucida Sans Typewriter',20,'normal'),width=2,textvariable=s)
seconds.place(x=140,y=20)
def check():
    try:
        temp=int(hours.get())*3600+int(minutes.get())*60+int(seconds.get())
    except:
        tkinter.messagebox.showerror('Error','Enter a valid input')
    while temp>-1:
        min,sec=divmod(temp,60)
        hr=00
        if min>60:
            hr,min=divmod(min,60)
        m.set('{:02d}'.format(min))
        s.set('{:02d}'.format(sec))
        h.set('{:02d}'.format(hr))
        window.update()
        time.sleep(1)
        temp-=1
        start.config(state='disabled')
        hours.config(state='disabled')
        minutes.config(state='disabled')
        seconds.config(state='disabled')
        if temp==0:
            tkinter.messagebox.showinfo('Finished','Time is up!')
start=Button(window,text='Start',font=('Lucida Sans Typewriter',9,'bold'),width=4,command=check)
start.place(x=170,y=65)
window.mainloop()