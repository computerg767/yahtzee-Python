from tkinter import *
import random

root = Tk()
# Variables Start

roll = 0

dicenames = ["one", "two", "three", "four", "five"]

dicenumbers = [0,0,0,0,0]

score = 0

for i in range(5):
    dicenames[i] = Button(root, text=dicenumbers[i], padx=15, pady=15)

for d in range(5):
    dicenames[d].grid(row=10, column=d)

root.mainloop()