from tkinter import *
from tkinter import font 
import random

window=Tk()
window.geometry('700x300')
window.title('Rock Paper Scissors')
window.config(background='gray13')
#fonts=font.families()
#print(fonts)
pscore=0
cscore=0
def game(player_choice):
    global cscore
    global pscore
    print(player_choice)
    items=['rock','paper','scissors']
    computer_choice=random.choice(items)
    yselect.config(text='You Selected: '+player_choice)
    cselect.config(text='Computer Selected: '+computer_choice)
    if (player_choice=='rock' and computer_choice=='paper') or (player_choice=='paper' and computer_choice=='scissors') or (player_choice=='scissors' and computer_choice=='rock'):
        title2.config(text='Computer Won!')
        cscore+=1
        compsc.config(text='Computer Score:'+str(cscore))

    elif player_choice==computer_choice:
        title2.config(text='Tie!')
    else:
        title2.config(text='You Won!')
        pscore+=1
        playersc.config(text='Player Score:'+str(pscore))
    


title=Label(window,bg='gray13',fg='white',text='Rock Paper Scissors',font=('System','20','normal'))
title.grid(row=1,column=1,padx=200)
title2=Label(window,bg='gray13',fg='green2',text='Sample',font=('System','15','normal'))
title2.grid(row=2,column=1,padx=230)
title3=Label(window,bg='gray13',fg='white',text='Your Options:',font=('System','16','normal'))
title3.place(x=30,y=70)
rock=Button(window,bg='white',fg='gray13',text='Rock',font=('System','16','normal'),width=15,command=lambda:game('rock'))
rock.place(x=40,y=100)
paper=Button(window,bg='white',fg='gray13',text='Paper',font=('System','16','normal'),width=15,command=lambda:game('paper'))
paper.place(x=200,y=100)
scissors=Button(window,bg='white',fg='gray13',text='Scissors',font=('System','16','normal'),width=15,command=lambda:game('scissors'))
scissors.place(x=360,y=100)
score=Label(window,bg='gray13',fg='white',text='Score:',font=('System','16','normal'))
score.place(x=30,y=150)
yselect=Label(window,bg='gray13',fg='white',text='You Selected:',font=('System','16','normal'))
yselect.place(x=80,y=180)
playersc=Label(window,bg='gray13',fg='white',text='Player Score:',font=('System','16','normal'))
playersc.place(x=300,y=180)
cselect=Label(window,bg='gray13',fg='black',text='Computer Selected:',font=('System','16','normal'))
cselect.place(x=80,y=210)
compsc=Label(window,bg='gray13',fg='black',text='Computer Score:',font=('System','16','normal'))
compsc.place(x=300,y=210)
window.mainloop()

