from tkinter import *
from tkinter import font 
import random
pscore=0
cscore=0
class rps():
    def __init__(self):
        self.window=Tk()
        self.window.geometry('700x300')
        self.window.title('Rock Paper Scissors')
        self.window.config(background='gray13')
        self.title=Label(self.window,bg='gray13',fg='white',text='Rock Paper Scissors',font=('System','20','normal'))
        self.title.grid(row=1,column=1,padx=200)
        self.title2=Label(self.window,bg='gray13',fg='green2',text='Sample',font=('System','15','normal'))
        self.title2.grid(row=2,column=1,padx=230)
        self.title3=Label(self.window,bg='gray13',fg='white',text='Your Options:',font=('System','16','normal'))
        self.title3.place(x=30,y=70)
        self.rock=Button(self.window,bg='white',fg='gray13',text='Rock',font=('System','16','normal'),width=15,command=lambda:self.game('rock'))
        self.rock.place(x=40,y=100)
        self.paper=Button(self.window,bg='white',fg='gray13',text='Paper',font=('System','16','normal'),width=15,command=lambda:self.game('paper'))
        self.paper.place(x=200,y=100)
        self.scissors=Button(self.window,bg='white',fg='gray13',text='Scissors',font=('System','16','normal'),width=15,command=lambda:self.game('scissors'))
        self.scissors.place(x=360,y=100)
        self.score=Label(self.window,bg='gray13',fg='white',text='Score:',font=('System','16','normal'))
        self.score.place(x=30,y=150)
        self.yselect=Label(self.window,bg='gray13',fg='white',text='You Selected:',font=('System','16','normal'))
        self.yselect.place(x=80,y=180)
        self.playersc=Label(self.window,bg='gray13',fg='white',text='Player Score:',font=('System','16','normal'))
        self.playersc.place(x=300,y=180)
        self.cselect=Label(self.window,bg='gray13',fg='black',text='Computer Selected:',font=('System','16','normal'))
        self.cselect.place(x=80,y=210)
        self.compsc=Label(self.window,bg='gray13',fg='black',text='Computer Score:',font=('System','16','normal'))
        self.compsc.place(x=300,y=210)
        self.window.mainloop()
        #fonts=font.families()
        #print(fonts)
    def game(self,player_choice):
        global cscore
        global pscore
        print(player_choice)
        items=['rock','paper','scissors']
        computer_choice=random.choice(items)
        self.yselect.config(text='You Selected: '+player_choice)
        self.cselect.config(text='Computer Selected: '+computer_choice)
        if (player_choice=='rock' and computer_choice=='paper') or (player_choice=='paper' and computer_choice=='scissors') or (player_choice=='scissors' and computer_choice=='rock'):
            self.title2.config(text='Computer Won!')
            cscore+=1
            self.compsc.config(text='Computer Score:'+str(cscore))

        elif player_choice==computer_choice:
            self.title2.config(text='Tie!')
        else:
            self.title2.config(text='You Won!')
            pscore+=1
            self.playersc.config(text='Player Score:'+str(pscore))
        
rps()
