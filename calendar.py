from tkinter import *
import calendar
window=Tk()   #creates a window
window.title('Calendar')  
window.geometry('260x160')
window.config(background='LightCyan2')
def getcalendar():
    user_input=int(year.get())
    #content=calendar.calendar(user_input)
    content=calendar.TextCalendar(calendar.SUNDAY).formatyear(user_input)
    screen=Tk()
    screen.title('Calendar')
    screen.geometry('500x500')
    screen.config(background='LightPink1')
    yearcalendar=Label(screen,bg='white',fg='black',text=content,font=('times',9,'bold'))
    yearcalendar.grid(row=1,column=1,padx=10)
    screen.mainloop()

title=Label(window, bg='white',fg='black',text='Calendar',font=('times',28,'bold'))
title.grid(row=1,column=1,padx=50)
title2=Label(window,bg='white',fg='black',text='Enter your year')
title2.grid(row=2,column=1,pady=6)
year=Entry()
year.grid(row=3,column=1)
submit=Button(window,text='Submit',command=getcalendar)
submit.grid(row=4,column=1,pady=6)
exit=Button(window,text='Exit',command=exit)
exit.place(x=220,y=130)
window.mainloop() #shows the screen forever