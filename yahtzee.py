from tkinter import *
import random

root = Tk()

root.title("Yatzee")
# Variables START

Roll = 0 

#DICE VARIABLES START
dice1 = 0
dice2 = 0
dice3 = 0 
dice4 = 0
dice5 = 0
# make dice global them global
def dice1_global():
    global dice1

dice1_global()

def dice2_global():
    global dice2

dice2_global()

def dice3_global():
    global dice3

dice3_global()

def dice4_global():
    global dice4

dice4_global()

def dice5_global():
    global dice5

dice5_global()
#DICE VARIABLES FINISH

#DICE CLICKED VARIABLES START

dice1_click = 1
dice2_click = 1 
dice3_click = 1
dice4_click = 1
dice5_click = 1

dice1_roll = 0
dice2_roll = 0
dice3_roll = 0
dice4_roll = 0
dice5_roll = 0 

score = 0

def score_glbl():
    global score

score_glbl()

# Variables END

#FUNCTIONS START
# creates a global to properly increment roll
def increment_roll(): 
    global Roll
    Roll = Roll+1

def dice1_clicked():
    global dice1_click
    global dice1_roll
    dice1_click = dice1_click+1
    if (dice1_click % 2) == 0:
        Dice_One.configure(fg="red")
        dice1_roll = 1
    else:
        Dice_One.configure(fg="black")
        dice1_roll = 0
        
def dice2_clicked():
    global dice2_click
    global dice2_roll
    dice2_click = dice2_click+1
    if (dice2_click % 2) == 0:
        Dice_Two.configure(fg="red")
        dice2_roll = 1
    else:
        Dice_Two.configure(fg="black")
        dice2_roll = 0

def dice3_clicked():
    global dice3_click
    global dice3_roll
    dice3_click = dice3_click+1
    if (dice3_click % 2) == 0:
        Dice_Three.configure(fg="red")
        dice3_roll = 1
    else:
        Dice_Three.configure(fg="black")
        dice3_roll = 0

def dice4_clicked():
    global dice4_click
    global dice4_roll
    dice4_click = dice4_click+1
    if (dice4_click % 2) == 0:
        Dice_Four.configure(fg="red")
        dice4_roll = 1
    else:
        Dice_Four.configure(fg="black")
        dice4_roll = 0

def dice5_clicked():
    global dice5_click
    global dice5_roll
    dice5_click = dice5_click+1
    if (dice5_click % 2) == 0:
        Dice_Five.configure(fg="red")
        dice5_roll = 1
    else:
        Dice_Five.configure(fg="black")
        dice5_roll = 0

def Roll_Dice():
    increment_roll()
    if dice1_roll == 0:
        dice1 = random.randint(1, 6)
        Dice_One.configure(text=dice1)
    if dice2_roll == 0:
        dice2 = random.randint(1, 6)
        Dice_Two.configure(text=dice2)
    if dice3_roll == 0:
        dice3 = random.randint(1, 6)
        Dice_Three.configure(text=dice3)
    if dice4_roll == 0:
        dice4 = random.randint(1, 6)
        Dice_Four.configure(text=dice4)
    if dice5_roll == 0:
        dice5 = random.randint(1, 6)
        Dice_Five.configure(text=dice5)
    if Roll == 3:
        Roll_btn.configure(state="disabled")

#FUNCTIONS END

#lABELS FOR RESULTS
score_lbl = Label (root, text=score, padx=100)
ones_lbl = Label (root, text="Ones")
twos_lbl = Label (root, text="Twos")
threes_lbl = Label (root, text="Threes")
fours_lbl = Label (root, text="Fours")
fives_lbl = Label (root, text="Fives")
sixs_lbl = Label (root, text="Sixs")
bonus_lbl = Label (root, text="Bonus")
threekind_lbl = Label (root, text="3x")
fourkind_lbl = Label (root, text="4x")
fh_lbl = Label (root, text="FH")
sm_lbl = Label (root, text="SM")
lg_lbl = Label (root, text="LG")
y_lbl = Label (root, text="Y")
chance_lbl = Label (root, text="?")
#BUTTONS START (BOTTOM)
ones_btn = Button(root, text="00", padx=10, pady=10)
twos_btn = Button(root, text="00", padx=10, pady=10)
threes_btn = Button(root, text="00", padx=10, pady=10)
fours_btn = Button(root, text="00", padx=10, pady=10)
fives_btn = Button(root, text="00", padx=10, pady=10)
sixs_btn = Button(root, text="00", padx=10, pady=10)
bonus_btn = Button(root, text="00", padx=10, pady=10)
threekind_btn = Button(root, text="00", padx=10, pady=10)
fourkind_btn = Button(root, text="00", padx=10, pady=10)
fh_btn = Button(root, text="00", padx=10, pady=10)
sm_btn = Button(root, text="00", padx=10, pady=10)
lg_btn = Button(root, text="00", padx=10, pady=10)
y_btn = Button(root, text="00", padx=10, pady=10)
chance_btn = Button(root, text="00", padx=10, pady=10)
Roll_btn = Button(root, text="Roll", padx=100, command=Roll_Dice)
Play_btn = Button(root, text="Play", padx=100, state="disabled")
Dice_One = Button(root, text=dice1, padx=15, pady=15, command=dice1_clicked)
Dice_Two = Button(root, text=dice2, padx=15, pady=15, command=dice2_clicked)
Dice_Three = Button(root, text=dice3, padx=15, pady=15, command=dice3_clicked)
Dice_Four = Button(root, text=dice4, padx=15, pady=15, command=dice4_clicked)
Dice_Five = Button(root, text=dice5, padx=15, pady=15, command=dice5_clicked)
#BUTTONS END (BOTTOM)

#LAYOUT START
score_lbl.grid(row=0, columnspan=5)
ones_lbl.grid(row=1, column=0)
ones_btn.grid(row=1, column=1)
threekind_lbl.grid(row=1, column=2)
threekind_btn.grid(row=1, column=3)
twos_lbl.grid(row=2, column=0)
twos_btn.grid(row=2, column=1)
fourkind_lbl.grid(row=2, column=2)
fourkind_btn.grid(row=2, column=3)
threes_lbl.grid(row=3, column=0)
threes_btn.grid(row=3, column=1)
fh_lbl.grid(row=3, column=2)
fh_btn.grid(row=3, column=3)
fours_lbl.grid(row=4, column=0)
fours_btn.grid(row=4, column=1)
sm_lbl.grid(row=4, column=2)
sm_btn.grid(row=4, column=3)
fives_lbl.grid(row=5, column=0)
fives_btn.grid(row=5, column=1)
lg_lbl.grid(row=5, column=2)
lg_btn.grid(row=5, column=3)
sixs_lbl.grid(row=6, column=0)
sixs_btn.grid(row=6, column=1)
y_lbl.grid(row=6, column=2)
y_btn.grid(row=6, column=3)
bonus_lbl.grid(row=7, column=0)
bonus_btn.grid(row=7, column=1)
chance_lbl.grid(row=7, column=2)
chance_btn.grid(row=7, column=3)
Roll_btn.grid(row=8, columnspan=5)
Play_btn.grid(row=9, columnspan=5)
Dice_One.grid(row=10, column=0)
Dice_Two.grid(row=10, column=1)
Dice_Three.grid(row=10, column=2)
Dice_Four.grid(row=10, column=3)
Dice_Five.grid(row=10, column=4)
#LAYOUT END
root.mainloop()