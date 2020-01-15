print("Question 8")
list1 = []
number = int(input("Enter a number between 0 and 100: "))
while number != -1:
    if number<-1 or number>100:
        number = int(input("That number is not valid. Enter a number between 0 and 100: "))
    else:
        list1.append(number)
        number = int(input("Enter a number between 0 and 100: "))
if number == -1:
    a = 0
    b = 0
    for number in list1:
        a += number
        b += 1
    if len(list1)>=1:
        print(list1)
        print("The average of all integers in this list is", round((a / b),5))
        print("The highest integer in this list is", max(list1))
        print("The lowest integer in this list is", min(list1))
    elif len(list1) == 0:
        print("This list is empty")
        print("There is no average")
        print("There are no integers in this list")
print("")


print("Question 9")
L1 = [1,6,5,3,7,6,21,8,4,2,8,9,2,5,7,3,5,45,2,6,8,1,9,7]
L2 = [12,65,23,76,34,87,45,34,76]

for x in L1:
    for y in L2:
        print(x,"x",y,"=",x*y)
print("")


print("Question 12")
height = int(input("Enter the size: "))
base = ((height * 2) - 1)
space = height - 1
stars = 1
for x in range(0,(height+1)):
    print(" "*space + "*"*stars)
    stars += 2
    space -= 1
    if stars == (base + 2):
        break
print("")