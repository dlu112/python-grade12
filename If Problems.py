print("Question 1")
copy = input("Enter the number of copies to be printed: ")
copy = int(copy)
if copy<0:
    price = 0
elif copy<100:
    price = 0.30
elif copy<500:
    price = 0.28
elif copy<750:
    price = 0.27
elif copy<=1000:
    price = 0.26
else:
    price = 0.25
print("Price per copy is: $",round(price,2))
total = copy*price
print("Total cost is: $",round(total,2))
print("")

print("Question 2")
weight = input("Enter package weight in kg: ")
length = input("Enter the package length in cm: ")
width = input("Enter the package width in cm: ")
height = input("Enter the package height in cm: ")
weight = int(weight)
length = int(length)
width = int(width)
height = int(height)
area = length*height*width
if weight>27 and area>100000:
    print("Package is too heavy and too big.")
elif weight>27:
    print("Package is too heavy.")
elif area>100000:
    print("Package is too large.")
else:
    print("Package approved.")
print("")

print("Question 3")
from random import randint
num1=randint(1,10)
num2=randint(1,10)
operator=randint(1,4)
if operator==1:
    question = input("What is %s + %s? " %(num1, num2))
    if float(question) == num1 + num2:
        print("Correct")
    else:
        print("Incorrect")
elif operator==2:
    question = input("What is %s * %s? " % (num1, num2))
    if float(question) == num1 * num2:
        print("Correct")
    else:
        print("Incorrect")
elif operator==3:
    question = input("What is %s - %s? " % (num1, num2))
    if float(question) == num1 - num2:
        print("Correct")
    else:
        print("Incorrect")
else:
    question = input("What is %s / %s (two decimal places)? " % (num1, num2))
    if float(question) == round(num1 / num2,2):
        print("Correct")
    else:
        print("Incorrect")