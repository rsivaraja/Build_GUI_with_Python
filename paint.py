from tkinter import*
from tkinter.colorchooser import askcolor
class Paint():
    def __init__(self):
        self.screen=Tk()
        self.screen.geometry('400x400')
        self.pen=Button(self.screen,text='pen',bg='white',fg='black',font=('Lucida Sans Typewriter',8,'normal'))
        self.pen.place(x=30,y=10)
        self.brush=Button(self.screen,text='brush',bg='white',fg='black',font=('Lucida Sans Typewriter',8,'normal'))
        self.brush.place(x=80,y=10)
        self.colour=Button(self.screen,text='colour',bg='white',fg='black',font=('Lucida Sans Typewriter',8,'normal'),command=self.choose_colour)
        self.colour.place(x=150,y=10)
        self.eraser=Button(self.screen,text='eraser',bg='white',fg='black',font=('Lucida Sans Typewriter',8,'normal'))
        self.eraser.place(x=220,y=10)
        self.size=Scale(self.screen,from_=1,to=5,orient=HORIZONTAL)
        self.size.place(x=290,y=0)
        self.paper=Canvas(self.screen,bg='white',width=400,height=390)
        self.paper.place(x=0,y=40)
        self.clr='black'
        self.screen.mainloop()
    def setup():
        pass
    def choose_colour(self):
        self.clr=askcolor(color=self.clr)[1]
        print(self.clr)


Paint()