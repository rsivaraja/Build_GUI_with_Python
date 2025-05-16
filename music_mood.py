from tkinter import*
import random
import webbrowser
window=Tk()
window.geometry('400x300')
songs={
    'Happy':[
      ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Can't Stop The Feeling - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw")  
    ],"Sad": [
        ("Someone Like You - Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA")
    ],
    "Relaxed": [
        ("Weightless - Marconi Union", "https://www.youtube.com/watch?v=UfcAVejslrU"),
        ("Bloom - The Paper Kites", "https://www.youtube.com/watch?v=8inJtTG_DuU")
    ],
    "Energetic": [
        ("Stronger - Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
        ("Eye of the Tiger - Survivor", "https://www.youtube.com/watch?v=btPJPFnesV4")
    ],
    "Angry": [
        ("Numb - Linkin Park", "https://www.youtube.com/watch?v=kXYiU_JCYtU"),
        ("In The End - Linkin Park", "https://www.youtube.com/watch?v=eVTXPUF4Oz4")
    ]
}
link=''
def reccomend():
    global link
    current_mood=endval1.get()
    song,link=random.choice(songs[current_mood])
    song_rec_label.config(text=song)
def open_link():
    global link
    webbrowser.open(link)



feeling_today=Label(window,fg='black',text='How are you feeling today?', font=('Lucida Sans Typewriter',10,'normal'))
feeling_today.place(x=100,y=20)
endval1=StringVar()
happy_button=Radiobutton(window,text='Happy',variable=endval1,value='Happy')
happy_button.place(x=10,y=30)
sad_button=Radiobutton(window,text='Sad',variable=endval1,value='Sad')
sad_button.place(x=10,y=50)
relaxed_button=Radiobutton(window,text='Relaxed',variable=endval1,value='Relaxed')
relaxed_button.place(x=10,y=70)
energetic_button=Radiobutton(window,text='Energetic',variable=endval1,value='Energetic')
energetic_button.place(x=10,y=90)
angry_button=Radiobutton(window,text='Angry',variable=endval1,value='Angry')
angry_button.place(x=10,y=110)
recommend_button=Button(window,fg='black',text='Recommend me a song',command=reccomend)
recommend_button.place(x=100,y=120)
song_rec_label=Label(window,fg='black',text='',font=('Lucida Sans Typewriter',9,'normal'))
song_rec_label.place(x=100,y=160)
play_button=Button(window,fg='black',text='Play song',command=open_link)
play_button.place(x=100,y=200)

window.mainloop()