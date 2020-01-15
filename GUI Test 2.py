import tkinter as tk
window = tk.Tk()

# Question Bank #
question1 = "Question 1: Q1"
question2 = "Question 2: Q2"
question3 = "Question 3: Q3"
question4 = "Question 4: Q4"
question5 = "Question 5: Q5"
question6 = "Question 6: Q6"
question7 = "Question 7: Q7"
question8 = "Question 8: Q8"
question9 = "Question 9: Q9"
question10 = "Question 10: Q10"

# Answer Bank #
answer1 = "a"
answer2 = "b"
answer3 = "c"
answer4 = "d"
answer5 = "e"
answer6 = "f"
answer7 = "g"
answer8 = "h"
answer9 = "i"
answer10 = "j"

# Hint Bank #
hint1 = "Incorrect. Hint: H1"
hint2 = "Incorrect. Hint: H2"
hint3 = "Incorrect. Hint: H3"
hint4 = "Incorrect. Hint: H4"
hint5 = "Incorrect. Hint: H5"
hint6 = "Incorrect. Hint: H6"
hint7 = "Incorrect. Hint: H7"
hint8 = "Incorrect. Hint: H8"
hint9 = "Incorrect. Hint: H9"
hint10 = "Incorrect. Hint: H10"


answer = answer1
hint = hint1


# Reply, wrong twice #
reply1 = "Wrong. The answer was: 'a'."
reply2 = "Wrong. The answer was: 'b'."
reply3 = "Wrong. The answer was: 'c'."
reply4 = "Wrong. The answer was: 'd'."
reply5 = "Wrong. The answer was: 'e'."
reply6 = "Wrong. The answer was: 'f'."
reply7 = "Wrong. The answer was: 'g'."
reply8 = "Wrong. The answer was: 'h'."
reply9 = "Wrong. The answer was: 'i'."
reply10 = "Wrong. The answer was: 'j'."


response = reply1

q1 = tk.Label(window, text=question1)
a1 = tk.Entry(window)
r1 = tk.Label(window)
question = 1
path = 0
points = 0
total = tk.Label(window, text=("Points:", points))


def buttonClick1():
    print("This just happened")
    global question
    global points
    global path
    reply = a1.get()
    if reply == answer:
        if path == 0:
            r1.config(text="Correct")
            b1.config(text="Next Question")
            points += 2
            total.config(text=("Points:", points))
            path = 3
            question += 1
        elif path == 2:
            r1.config(text="Correct")
            b1.config(text="Next Question")
            points += 1
            total.config(text=("Points:", points))
            path = 3
            question += 1
    elif reply != answer:
        if path == 2:
            r1.config(text=response)
            b1.config(text="Next Question")
            path = 3
            question += 1
        elif path == 0:
            r1.config(text=hint)
            path = 2
    if path == 3:
        b1.config(command=buttonClickNext)


b1 = tk.Button(window, text="Confirm", command=buttonClick1)


def buttonClickNext():
    global hint
    global answer
    global path
    global response
    print("buttonClickNext just happened")
    if question == 2:
        q1.config(text=question2)
        b1.config(text="Confirm")
        answer = answer2
        hint = hint2
        response = reply2
        path = 0
        b1.config(command=buttonClickReset)
    elif question == 3:
        q1.config(text=question3)
        b1.config(text="Confirm")
        answer = answer3
        hint = hint3
        response = reply3
        path = 0
        b1.config(command=buttonClickReset)
    elif question == 4:
        q1.config(text=question4)
        b1.config(text="Confirm")
        answer = answer4
        hint = hint4
        response = reply4
        path = 0
        b1.config(command=buttonClickReset)
    elif question == 5:
        q1.config(text=question5)
        b1.config(text="Confirm")
        answer = answer5
        hint = hint5
        response = reply5
        path = 0
        b1.config(command=buttonClickReset)
    elif question == 6:
        q1.config(text=question6)
        b1.config(text="Confirm")
        answer = answer6
        hint = hint6
        response = reply6
        path = 0
        b1.config(command=buttonClickReset)
    elif question == 7:
        q1.config(text=question7)
        b1.config(text="Confirm")
        answer = answer7
        hint = hint7
        response = reply7
        path = 0
        b1.config(command=buttonClickReset)
    elif question == 8:
        q1.config(text=question8)
        b1.config(text="Confirm")
        answer = answer8
        hint = hint8
        response = reply8
        path = 0
        b1.config(command=buttonClickReset)
    elif question == 9:
        q1.config(text=question9)
        b1.config(text="Confirm")
        answer = answer9
        hint = hint9
        response = reply9
        path = 0
        b1.config(command=buttonClickReset)
    elif question == 10:
        q1.config(text=question10)
        b1.config(text="Confirm")
        answer = answer10
        hint = hint10
        response = reply10
        path = 0
        b1.config(command=buttonClickReset)
    else:
        q1.config(text="Congratulations!")
        b1.config(text="", command="")
        r1.config(text=("Score:", points, "points"))


def buttonClickReset():
    b1.config(command=buttonClick1())


total.grid(row=2, column=2, sticky="W")
q1.grid(row=2, column=1)
b1.grid(row=3, column=2)
a1.grid(row=3, column=1)
r1.grid(row=4, column=1)


window.mainloop()
