from tkinter import *
window=Tk()
window.geometry('260x160')
window.title('Celsius to Farenheit Converter')
def gettemp():
    try:
        user_input=int(temp.get())
    except ValueError:
        msg=Label(window,fg='red',text='Please enter valid input...')
        msg.place(x=120,y=80)
    user_input=(user_input*9/5)+32
    answer.config(text='Temperature in Farenheit:'+str(user_input))
title=Label(window, fg='grey', text='Celsius -> Farenheit', font=('times',18,'bold'))
title.grid(row=1,column=1,padx=15)
title2=Label(window,fg='black',text='Enter Temperature in Celsius:')
title2.grid(row=2,column=1,pady=6)
temp=Entry()
temp.grid(row=3,column=1)
answer=Label(window,fg='black',text='Temperature in Farenheit:',font=(9))
answer.grid(row=4,column=1)
convert=Button(window,text='Convert',bg='green yellow',width=15,command=gettemp)
convert.place(x=65,y=111)
window.mainloop()