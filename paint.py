from tkinter import*
from tkinter.colorchooser import askcolor
class Paint():
    def __init__(self):
        self.screen=Tk()
        self.screen.geometry('500x500')
        self.pen=Button(self.screen,text='pen',bg='white',fg='black',font=('Lucida Sans Typewriter',8,'normal'),command=self.draw)
        self.pen.place(x=30,y=10)
        self.brush=Button(self.screen,text='brush',bg='white',fg='black',font=('Lucida Sans Typewriter',8,'normal'),command=self.paint)
        self.brush.place(x=80,y=10)
        self.colour=Button(self.screen,text='colour',bg='white',fg='black',font=('Lucida Sans Typewriter',8,'normal'),command=self.choose_colour)
        self.colour.place(x=150,y=10)
        self.eraser=Button(self.screen,text='eraser',bg='white',fg='black',font=('Lucida Sans Typewriter',8,'normal'),command=self.erase)
        self.eraser.place(x=220,y=10)
        self.size=Scale(self.screen,from_=1,to=5,orient=HORIZONTAL)
        self.size.place(x=290,y=0)
        self.clear=Button(self.screen,text='clear',bg='white',fg='black',font=('Lucida Sans Typewriter',8,'normal'),command=self.remove)
        self.clear.place(x=410,y=10)
        self.paper=Canvas(self.screen,bg='white',width=500,height=490)
        self.paper.place(x=0,y=40)
        self.clr='black'
        self.setup()
        self.screen.mainloop()
    def setup(self):
        self.old_x=None
        self.old_y=None
        self.clr='black'
        self.eraser_on=False
        self.active_button=self.pen
        self.paper.bind('<B1-Motion>',self.create)
        self.paper.bind('<ButtonRelease-1>',self.not_create)
    def choose_colour(self):
        self.clr=askcolor(color=self.clr)[1]
        print(self.clr)
    def draw(self):
        self.activate(self.pen)
    def paint(self):
        self.activate(self.brush)
    def remove(self):
        self.activate(self.clear)
        self.paper.delete('all')
    def erase(self):
        self.activate(self.eraser,eraser_mode=True)
    def activate(self,btn,eraser_mode=False):
        self.active_button.config(relief=RAISED)
        btn.config(relief=SUNKEN)
        self.eraser_on=eraser_mode
        self.active_button=btn
    def create(self,e):
        if self.eraser_on==True:
            paint_colour='white'
        else:
            paint_colour=self.clr
        if self.active_button==self.brush:
            self.line_width=self.size.get()+10
        else:
            self.line_width=self.size.get()

        if self.old_x and self.old_y:
            self.paper.create_line(self.old_x,self.old_y,e.x,e.y,fill=paint_colour,width=self.line_width)
        self.old_x=e.x
        self.old_y=e.y
    def not_create(self,e):
        self.old_x=None
        self.old_y=None

            
Paint()