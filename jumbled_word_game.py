from tkinter import*
from tkinter import messagebox
import random
window=Tk()
window.title('Jumbled word game')
window.geometry('250x350')
window.config(background='SpringGreen4')
user_score=0
words=['apple','blue','charisma','dog','example','friend','great','happy','indigo','jewellery','kids','laughter','mother','nothing','otherwise']
words_jumbled=['pleap','elub','amrischa','ogd','elexmap','dferin','tagre','hypap','igdoin','eyljewlre','sikd','aghuetlr','htoerm','gonhitn','whtosiere']
number=random.randint(0,14)
word=words_jumbled[number]
def replace():
    global number
    global word
    number=random.randint(0,14)
    word=words_jumbled[number]
    jumbled_word.config(text=word)
    answer.delete(0,END)
def confirm():
    user_answer=answer.get()
    global words
    global number
    print(number)
    if user_answer==words[number]:
        global user_score
        user_score+=1
        messagebox.showinfo('Correct','Your answer is correct!')
        score.config(text=f'Score:{user_score}')
        replace()
    else:
        messagebox.showinfo('Incorrect','Unfortunately, your answer is incorrect')
        replace()

title=Label(bg='black',fg='white',text='Jumbled word game',font=('Lucida Sans Typewriter',13,'normal'))
title.place(x=50,y=30)
answer=Entry(width=15)
answer.place(x=90,y=120)
check=Button(bg='gray51',fg='green3',text='Check',font=('Lucida Sans Typewriter',11,'normal'),command=confirm)
check.place(x=100,y=160)
reset=Button(bg='gray51',fg='gold',text='Reset',font=('Lucida Sans Typewriter',11,'normal'),command=replace)
reset.place(x=100,y=200)
jumbled_word=Label(bg='black',fg='white',text=word,font=('Lucida Sans Typewriter',12,'normal'))
jumbled_word.place(x=100,y=75)
score=Label(bg='black',fg='white',text=f'Score:{user_score}',font=('Lucida Sans Typewriter',10,'normal'))
score.place(x=0,y=250)
window.mainloop()