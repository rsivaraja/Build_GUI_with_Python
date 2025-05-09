from tkinter import*
from tkinter import filedialog
import os
import pygame
pygame.mixer.init()
window=Tk()
window.geometry('600x300')
window.title('Music Player')
song_status=Label(window,text='No song loaded', fg='black',font=('Lucida Sans Typewriter',12,'normal'))
current_song=''
paused=False
current_index=0
playlist=[]
def load_music():
    global current_song
    global current_index
    global playlist
    file=filedialog.askopenfilenames(filetypes=[('Audio Files','*.mp3 *.wav *.ogg')])
    if file:
        playlist=list(file)
        current_song=file[current_index]
        text=os.path.basename(current_song)
        song_status.config(text=text)
def play_music():
    global current_song
    global paused
    if paused==True:
        pygame.mixer.music.unpause()
        paused=False
    else:
        current_song=playlist[current_index]
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused=True
def stop_music():
    pygame.mixer.music.stop()
def set_volume(value):
    volume=int(value)/100
    pygame.mixer.music.set_volume(volume)
def load_previous():
    global current_index,current_song
    if playlist and current_index>0:
        current_index-=1
        current_song=playlist[current_index]
        play_music()
    text=os.path.basename(current_song)
    song_status.config(text=text)
def load_next():
    global current_index,current_song
    if playlist and current_index<len(playlist):
        current_index+=1
        current_song=playlist[current_index]
        play_music()
    text=os.path.basename(current_song)
    song_status.config(text=text)
song_status.place(x=100,y=10)
load=Button(window,text='Load',width=9,font=('Lucida Sans Typewriter',10,'normal'),command=load_music)
load.place(x=90,y=90)
play=Button(window,text='Play ▶️',width=9,font=('Lucida Sans Typewriter',10,'normal'),command=play_music)
play.place(x=200,y=90)
pause=Button(window,text='Pause ⏸️',width=9,font=('Lucida Sans Typewriter',10,'normal'),command=pause_music)
pause.place(x=310,y=90)
stop=Button(window,text='Stop ⏹️',width=9,font=('Lucida Sans Typewriter',10,'normal'),command=stop_music)
stop.place(x=420,y=90)
volume=Label(window,text='Volume',fg='black',font=('Lucida Sans Typewriter',11,'normal'))
volume.place(x=260,y=150)
volume_adjuster=Scale(window,from_=0,to=100,orient=HORIZONTAL,command=set_volume)
volume_adjuster.place(x=240,y=180)
previous=Button(window,text='Previous',fg='black',font=('Lucida Sans Typewriter',10,'normal'),command=load_previous)
previous.place(x=140,y=200)
next=Button(window,text='Next',fg='black',font=('Lucida Sans Typewriter',10,'normal'),command=load_next)
next.place(x=380,y=200)

window.mainloop()