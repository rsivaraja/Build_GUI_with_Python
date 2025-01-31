from tkinter import*
from time import strftime
import random
colours=['IndianRed1','maroon','brown4','OrangeRed2','firebrick1']
colours2=['salmon','LightPink1','pale violet red','snow']

window=Tk()
window.title('Digital Clock')
window.geometry('260x100')
time=Label(window,fg='black',text='',font=('Lucida Sans Typewriter',20,'normal'))
time.pack(anchor='center')
def clock():
    current_time=strftime('%H:%M:%S')
    time.config(text=current_time)
    c1 = "#"+"".join([random.choice("0123456789ABCDEF") for i in range(6)] )
    c2= "#"+"".join([random.choice("0123456789ABCDEF") for i in range(6)] )
    window.config(background=c1)
    time.config(bg=c1,fg=c2)
    time.after(1000,clock)
clock()
window.mainloop()