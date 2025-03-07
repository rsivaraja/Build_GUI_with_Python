from tkinter import*
from gtts import gTTS
import os
from translate import Translator
from tkinter.ttk import*
window=Tk()
window.geometry('300x400')
window.title('Text to Speech')
def spanish():
    language=selection.get()
    translator=Translator(to_lang=language)
    entry=entry_box.get()
    translated_text=translator.translate(entry)
    sound=gTTS(text=translated_text,lang=language,slow=False)
    sound.save('text_translated.mp3')
    os.system('text_translated.mp3')


selection=StringVar()
world={'Spanish':'es','French':'fr','German':'de'}
ypos=160
for key,value in world.items():
    Radiobutton(window,text=key,variable=selection,value=value).place(x=190,y=ypos)
    ypos+=20

# r1=Radiobutton(window,text='Spanish',variable=selection,value='es')
# r2=Radiobutton(window,text='French',variable=selection,value='fr')
# r3=Radiobutton(window,text='German',variable=selection,value='de')
# r1.place(x=190,y=160)
# r2.place(x=190,y=180)
# r3.place(x=190,y=200)
title=Label(window,text='Text to Speech',font=('Lucida Sans Typewriter',13,'normal'))
title.place(x=60,y=25)
entry_box=Entry(window,width=15,font=('Lucida Sans Typewriter',12,'normal'))
entry_box.place(x=60,y=100)
submit=Button(window,text='Submit',command=spanish)
submit.place(x=100,y=140)

window.mainloop()