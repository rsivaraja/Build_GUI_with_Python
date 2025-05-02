from tkinter import*
from tkinter import filedialog
import pygame
pygame.mixer.init()
window=Tk()
window.geometry('600x300')
window.title('Music Player')
song_status=Label(window,text='No song loaded', fg='black',font=('Lucida Sans Typewriter',12,'normal'))
current_song=''
paused=False
def load_music():
    global current_song
    file=filedialog.askopenfilename(filetypes=[('Audio Files','*mp3*.wav*.ogg')])
song_status.place(x=230,y=10)
load=Button(window,text='Load',width=9,font=('Lucida Sans Typewriter',10,'normal'),command=load_music)
load.place(x=90,y=90)
play=Button(window,text='Play ▶️',width=9,font=('Lucida Sans Typewriter',10,'normal'))
play.place(x=200,y=90)
pause=Button(window,text='Pause ⏸️',width=9,font=('Lucida Sans Typewriter',10,'normal'))
pause.place(x=310,y=90)
stop=Button(window,text='Stop ⏹️',width=9,font=('Lucida Sans Typewriter',10,'normal'))
stop.place(x=420,y=90)
volume=Label(window,text='Volume',fg='black',font=('Lucida Sans Typewriter',11,'normal'))
volume.place(x=260,y=150)
volume_adjuster=Scale(window,from_=0,to=100,orient=HORIZONTAL)
volume_adjuster.place(x=240,y=180)



window.mainloop()