from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

#TODO: Reading the csv file
try:
    data = pandas.read_csv("data/words_to_learn")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records", index=False)
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    """This function randomly selects a random French word anytime the button is clicked but automatically changes in 3 seconds"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,fill="black", text="French")
    canvas.itemconfig(card_word,fill="black", text=current_card["French"])
    canvas.itemconfig(card_img, image=front_img)
    flip_timer = window.after(3000, func=flipcard)


def flipcard():
    global current_card
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(card_title, fill="White", text="English")
    canvas.itemconfig(card_word, fill="white" ,text=current_card["English"])

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn")
    next_card()


#TODO: Creating the UI setup
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flipcard)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400,150, text="", font=("Ariel",40,'italic'))
card_word = canvas.create_text(400,263, text="", font=("Ariel",60,'bold'))
canvas.grid(row=0, column=0, columnspan=2)

check_img = PhotoImage(file="images/right.png")
known_btn = Button(image=check_img, highlightthickness=0, command=is_known)
known_btn.grid(row=1, column=1)

cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)



next_card()














window.mainloop()
