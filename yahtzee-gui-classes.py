from tkinter import *
import random
from functools import partial

root = Tk()

root.title("Yahtzee")

# Variables Start

roll = 0

dicenames = ["one", "two", "three", "four", "five"]

dicenumbers = [0,0,0,0,0]

diceclicked = [1,1,1,1,1]

score = 0

def click(n):
    diceclicked[n] = diceclicked[n] + 1
    if (diceclicked[n] % 2) == 0:
        dicenames[n].configure(background="red", activebackground="red")
    else:
        dicenames[n].configure(background="black", activebackground="black")



for i in range(5):
    dicenames[i] = Button(root, state="normal", relief="raised", text=dicenumbers[i], padx=15, pady=15, command=partial(click, i))
    dicenames[i].grid(row=10, column=i)

root.mainloop()