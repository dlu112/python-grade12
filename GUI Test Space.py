import tkinter as tk
import time
window = tk.Tk()

clicks=0
attempts=0
success=0

confirmlabel2=tk.Label(window, text="What is your name?")
textBox1=tk.Entry(window)


def buttonClick():
    global clicks
    confirmlabel1 = tk.Label(window)
    enteredName=textBox1.get()
    confirmlabel2.config(text=("Hello",enteredName))
    confirmlabel1 = tk.Label(window)
    confirmlabel1.config(text="Quick, defuse the bomb! One defuses, three detonate!")
    def wire1():
        def buttonClick1():
            global success
            global attempts
            button1.config(text=str("____________/  \___________"))
            if attempts == 0:
                confirmlabel1.config(text="BOOM!")
            elif success == 1:
                confirmlabel1.config(text="Good job!")
            else:
                confirmlabel1.config(text="Too late!")
            attempts += 1

        button1 = tk.Button(window, text="__________________________", command=buttonClick1)
        button1.pack()
    def wire2():
        def buttonClick2():
            global success
            global attempts
            button2.config(text=str("____________/  \___________"))
            if attempts == 0:
                confirmlabel1.config(text="BOOM!")
            elif success == 1:
                confirmlabel1.config(text="Good job!")
            else:
                confirmlabel1.config(text="Too late!")
            attempts += 1

        button2 = tk.Button(window, text="__________________________", command=buttonClick2)
        button2.pack()
    def wire3():
        def buttonClick3():
            global success
            global attempts
            button3.config(text=str("____________/  \___________"))
            if attempts == 0:
                confirmlabel1.config(text="BOOM!")
            elif success == 1:
                confirmlabel1.config(text="Good job!")
            else:
                confirmlabel1.config(text="Too late!")
            attempts += 1

        button3 = tk.Button(window, text="__________________________", command=buttonClick3)
        button3.pack()
    def wire4():
        def buttonClick4():
            global success
            global attempts
            button4.config(text=str("____________/  \___________"))
            if attempts == 0:
                confirmlabel1.config(text="Defused!")
                success +=1
            elif success == 1:
                confirmlabel1.config(text="Good job!")
            else:
                confirmlabel1.config(text="Too late!")
            attempts += 1

        button4 = tk.Button(window, text="__________________________", command=buttonClick4)
        button4.pack()
    confirmlabel1.pack()
    if clicks == 0:
        wire1()
        wire2()
        wire3()
        wire4()
        clicks +=1
button = tk.Button(window, text="Confirm", command=buttonClick)



confirmlabel2.pack()
textBox1.pack()
button.pack()




window.mainloop()