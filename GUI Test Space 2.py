import tkinter as tk
from random import randint
from tkinter import *

window = tk.Tk()

title = tk.Label(window, text="                             Dice Roller")
numdice = tk.Label(window, text="How many dice do you want to roll?")
v = 1
numroll = tk.Label(window, text=v)
resultbox = tk.Label(window)
numside = tk.Label(window, text="How many sides do your dice have?")
sidebar = tk.Scale(window, from_=2, to=20, orient=HORIZONTAL)

def buttonClick2():
    global v
    v += 1
    numroll.config(text=v)
plusbutton = tk.Button(window, text="+", command=buttonClick2)

def buttonClick3():
    global v
    if v > 1:
        v -= 1
        numroll.config(text=v)
subbutton = tk.Button(window, text="-", command=buttonClick3)

def buttonClick1():
    results = []
    maximum = sidebar.get()
    for x in range(v):
        result = randint(1, maximum)
        results.append(result)
    resultbox.config(text=results)
rollbutton = tk.Button(window, text="Roll", command=buttonClick1)

title.grid(columnspan=2, sticky=W)
numside.grid(row=2, column=1)
sidebar.grid(row=3, column=1)
numdice.grid(row=4, column=1)
subbutton.grid(row=5, column=0)
numroll.grid(row=5, column=1)
plusbutton.grid(row=5, column=2)
rollbutton.grid(row=6, column=1)
resultbox.grid(row=7, column=1)

window.mainloop()
