print ("Question 1")
time = input("How many seconds has the object been falling for?")
height = 100-4.9*float(time)**2
print ("The object is at", round(height,2), "meters.")
print ("")
#------------------------------------------------------------------------------------------#
print ("Question 2")
temp = input("Enter the current temperature in Fahrenheit")
celsius = (5.00/9.00)*(float(temp)-32)
print ("The temperature in Celsius is", round(celsius, 2), "degrees.")
print ("")
#------------------------------------------------------------------------------------------#
print ("Question 3")
dia = input("What is the diameter of the pizza?")
cost = 1.20+0.05*round(float(dia), 2)**2.00
print ("The cost of the pizza is $",round(cost,2))
print ("")
#------------------------------------------------------------------------------------------#
print ("Question 4")
first = input("Pick an integer:")
second = input("Pick another integer:")
eq1 = float(first)//float(second)
eq2 = float(first)%float(second)
eq3 = float(second)//float(first)
eq4 = float(second)%float(first)
print (first, "//", second, "=", round(eq1, 3))
print (first, "%", second, "=", round(eq2, 3))
print (second, "//", first, "=", round(eq3, 3))
print (second, "%", first, "=", round(eq4, 3))
print ("")
#------------------------------------------------------------------------------------------#
print ("Question 5")
minutes = input("Enter the number of minutes:")
min = int(minutes)%60
hour = int(minutes)//60
if min<10:
   print ("This is %s:0%s" % (hour, min))
else:
   print ("This is %s:%s" % (hour, min))
print ("")
#------------------------------------------------------------------------------------------#
print ("Question 6")
change = input("Enter the amount of change in cents:")
quarters = int(change)//25
dimes = (int(change)%25)//10
nickels = ((int(change)%25)%10)//5
pennies = (((int(change)%25)%10)%5)
print ("Change:")
print ("Quarters", quarters)
print ("Dimes:", dimes)
print ("Nickels:", nickels)
print ("Pennies:", pennies)
print ("")
#------------------------------------------------------------------------------------------#
print ("Question 7a")
burg = input("Enter the number of burgers:")
fry = input("Enter the number of fries:")
soda = input("Enter the number of sodas:")
priceb = int(burg)*1.49
pricef = int(fry)*0.89
prices = int(soda)*0.99
pretax = priceb+pricef+prices
print ("The total before tax is $",round(pretax,2))
tax = pretax*0.06
total = pretax+tax
print ("The total is $",round(total,2))
print ("")
#------------------------------------------------------------------------------------------#
print ("Question 7b")
amount = input("Enter the amount tendered:")
change = float(amount)-total
print ("The change is $",round(change,2))
print ("")
#------------------------------------------------------------------------------------------#
print ("Question 8a")
pots = input("Enter the number of flower pots to ship:")
big = int(pots)//4
small = int(pots)%4
print ("We will ship:")
print (big, "large box(es)")
print (small, "small box(es)")
print ("")
#------------------------------------------------------------------------------------------#
print ("Question 8b")
pots = input("Enter the number of flower pots to ship:")
very_big = int(pots)//9
big = (int(pots)%9)//4
small = (int(pots)%9)%4
print ("We will ship:")
print (very_big, "very large box(es)")
print (big, "large box(es)")
print (small, "small box(es)")
print ("")
