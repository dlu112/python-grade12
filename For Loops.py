text = input("Enter a sentence or quote: ").lower()
char = input("What character are you looking for? ").lower()
print("The character",char,"appears",text.count(char),"times.")
print("The character appears at the following indexes:")
a=0
for x in text:
    if x == char:
        index = (text.find(char))
        print(index+a)
    text = text.lstrip(x)
    a+=1

print("")
input("STOP")




first = input("What is your first name? ")
middle = input("What is your middle name? ")
last = input("What is your last name? ")
first=first.lower()
middle=middle.lower()
last=last.upper()
monogram = first[0] + last[0] + middle[0]
print(monogram)




from random import randint
num1=randint(1,6)
num2=randint(1,6)+randint(1,6)+randint(1,6)
num3=randint(1,6)
print(num1)
print(num2)
print(num3)
total=0
for x in range(num1, num2, num3):
    total+=x
print(total)

#-------------------------------------------------------------------#
#Question 5#

first=int(input("Enter the first (one digit) number: "))
second=int(input("Enter the second (one digit) number: "))
num1=first
num2=second
print(num1)
print(num2)
next=0
while num2 != first or next != second:
    next=num1+num2
    if next>=10:
        next-=10
    print(next)
    num1=num2
    if num2==first and next==second:
        break
    num2=next
print("")

#-------------------------------------------------------------------#
#Question 4#

max=int(input("Enter the maximum number: "))
total = 0
number = 1
for x in range(max):
    total += number
    number += 2
    if number>=max:
        break
print(total)
print("")

#-------------------------------------------------------------------#
#Question 3#

number = 20
for x in range(20):
    print(number)
    number-=1
print("")

#-------------------------------------------------------------------#
#Question 2#

number =2
for x in range(10):
    print(number)
    number+=2
print("")

#-------------------------------------------------------------------#
#Question 1#

from random import randint
rolls=int(input("How many rolls do you want to make? "))
print("Die 1    Die 2    Total")
for x in range(rolls):
    total=0
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    total+=roll1+roll2
    print("   ",roll1,"      ",roll2,"      ",total)
print("")

#-------------------------------------------------------------------#

num=int(input("Enter a number: "))
stars=""
for x in range(num):
    stars+="*"
    print(stars)


size=int(input("Size? "))
stars=""
for x in range(1,size+1):
    for z in range(1,x+1):
        stars+="*"
    print(stars)
    stars=""


number=input("Enter a number: ")
total = 0
for x in number:
    x=int(x)
    total += x
print(total)

for x in range(-5,4):
    print("We're on time ", x)

for letter in "MontyPython":
    print("Current letter: ", letter)

for letter in "ABC123":
    print("Current letter: ", letter)

fruits = ["banana", "apple", "orange"]
for fruit in fruits:
    print("Current fruit:", fruit)

year=int(input("How old are you? "))
for x in range(year):
    print("Happy birthday!", x+1)