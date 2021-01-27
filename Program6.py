print("Program6")
from  tkinter import  *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Data Flair - Rock-Paper-Scissor')
root.config(bg = 'seashell3')

Label(root, text = 'Rock-Paper-Scissor', font = 'arial 20 bold', bg = 'seashell2').pack()

user_take = StringVar()
Result = StringVar()
comp_pick = ""

def Comp():
    comp_pick = random.randint(1, 3)
    if comp_pick == 1:
        comp_pick = 'Rock'
    elif comp_pick == 2:
        comp_pick = 'Paper'
    else:
        comp_pick = "Scissor"
    return comp_pick

def Reset():
    Result.set("")
    user_take.set("")

def Rock():
    if (Comp() == "Scissor"):
        Result.set("You Win!\nComputer chose Scissor.")
    elif (Comp() == "Paper"):
        Result.set("You Lose!\nComputer chose Paper.")
    else:
        Result.set("TIE!")
def Paper():
    if (Comp() == "Scissor"):
        Result.set("You Lose!\nComputer chose Scissor.")
    elif (Comp() == "Paper"):
        Result.set("TIE")
    else:
        Result.set("You Win!\nComputer chose Rock")
def Scissor():
    if (Comp() == "Rock"):
        Result.set("You Lose!\nComputer chose Scissor.")
    elif (Comp() == "Paper"):
        Result.set("You Win!\nComputer chose Paper.")
    else:
        Result.set("TIE!")



def Exit():
    root.destroy()

Label(root, text = 'Choose anyone : Rock-Paper-Scissor', font = 'arial 15 bold', bg = 'seashell2').place(x=20, y=70)
Button(root, font = 'arial 13 bold', text = "ROCK", padx = 5, bg = 'seashell4', command = Rock).place(x=40, y=130)
Button(root, font = 'arial 13 bold', text = "PAPER", padx = 5, bg = 'seashell4', command = Paper).place(x=160,y=130)
Button(root, font = 'arial 13 bold', text = "SCISSOR",  padx = 5, bg = 'seashell4', command = Scissor).place(x=280, y=130)

Entry(root, font = 'arial 10 bold', textvariable = Result, bg = 'antiquewhite2', width = 50, ).place(x=25, y=250)
Button(root, font = 'arial 13 bold', text = "RESET", padx = 5, bg = 'seashell4', command = Reset).place(x=80,y=310)
Button(root, font = 'arial 13 bold', text = "EXIT",  padx = 5, bg = 'seashell4', command = Exit).place(x=240, y=310)

root.mainloop()