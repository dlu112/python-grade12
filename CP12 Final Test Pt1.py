print("Question 1")
firstname = input("What is your first name? ")
print("Hello ", firstname.capitalize(),"!", sep="")
lastname = input("What is your last name? ")
print("The", lastname.capitalize(), "family is very famous.")
print("")


print("Question 2")
favcolour = input("What is your favourite colour? ")
print("Thank you")
favnumber = input("What is your favourite number? ")
print("A", favcolour.lower(), favnumber.lower(), "is a sign of good luck.")
print("")


print("Question 3: Division")
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
type = input("What type of division do you want to do? (standard, integer, or modular) ")
if type.lower() == "standard":
    print(first,"/",second,"=",round((first/second), 5))
elif type.lower() == "integer":
    print(first,"//",second,"=",first//second)
elif type.lower() == "modular":
    print(first,"%",second,"=",first%second)
print("")


print("Question 4: Sorting numbers")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the last number: "))
if number1 >= number2:
    b = number1
    number1 = number2
    number2 = b
if number2 >= number3:
    b = number2
    number2 = number3
    number3 = b
    if number1 >= number2:
        b = number1
        number1 = number2
        number2 = b
print(number1, number2, number3)
print("")


print("Question 5: Prime factorization")
bignumber = int(input("Enter a number: "))
integer = 2
original = bignumber
text1 = ""
while integer <= bignumber:
    if bignumber%integer == 0:
        text1 += str(integer)
        if integer != bignumber:
            text1 += " x "
        else:
            text1 += (" = " + str(original))
        bignumber = bignumber//integer
    else:
        integer += 1
print(text1)
print("")


print("Question 6: Product sum of square roots")
mainnum = int(input("Enter a number: "))
total = 1
mainnum += 1
for x in range(1, mainnum):
    total *= x**(1/2)
print(round(total, 5))
print("")


print("Question 7")
number = int(input("Enter the number of perfect cubes you want multiplied: "))
total = 0
text = ""
number+=1
for x in range(1, number):
    text += (str(x))
    text += "**3"
    if x != (number-1):
        text += " + "
    else:
        text += " = "
    total += x**3
print(text + str(total))
print("")