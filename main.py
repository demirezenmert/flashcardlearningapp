BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from data import Data

# timer= None

#-------------French Card-----------#




def next_french_card():
    
    global timer
    try:
        window.after_cancel(timer)
    except NameError:
        pass
    
    
    try:
        card_data.random_pick()
    except (IndexError, ValueError):
        canvas.itemconfig(title_question,text='Well Done!',fill='Black')
        canvas.itemconfig(answer,text="You've meorized every card in this set.",fill='Black')

    canvas.itemconfig(canvas_img,image=canvas_img_front)
    canvas.itemconfig(title_question,text='French',fill='Black')
    canvas.itemconfig(answer,text=card_data.current_f_card,fill='Black')
    timer= window.after(3000,flip_card)
    

def flip_card():

    canvas.itemconfig(canvas_img,image=canvas_img_back)
    canvas.itemconfig(title_question,text='English', fill='White')
    canvas.itemconfig(answer,text=card_data.current_e_card, fill='White')

def is_known():
    card_data.need_to_learn()
    next_french_card()

window= Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
try:
    card_data= Data('data/words_to_learn.csv')
except:
    card_data= Data('data/french_words.csv')

canvas= Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_img_front= PhotoImage(file='images/card_front.png')
canvas_img_back= PhotoImage(file='images/card_back.png')
canvas_img= canvas.create_image(400,265,image=canvas_img_front)
title_question=canvas.create_text(400,150,text='French',fill='black',font=('Ariel',40,'italic'))
answer=canvas.create_text(400,263,text='trouve',fill='black',font=('Ariel',60,'bold'))
canvas.grid(column=0,row=0,columnspan=2)

right_my_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_my_image, highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)
wrong_my_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_my_image, highlightthickness=0,command=flip_card)
wrong_button.grid(column=0,row=1)
next_french_card()


window.mainloop()