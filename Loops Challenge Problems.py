#PART ONE#
list=[]
total=int(input("How many numbers do you want to sort? "))
for x in range(0, total):
    list.append(int(input("Enter a number ")))
print(list)
list.sort()
print(list)
print("")

#PART TWO#
invest=2500
years=0
print("Initial = $", round(invest,2))
while invest<5000:
    invest=invest*1.075
    years+=1
    print("Year", years)
    print("Total = $", round(invest,2))
print("")

#BONUS#
invest=float(input("How much money do you want to invest now? $"))
total=float(input("How much money do you want to have at the end? $"))
rate=float(input("What annual compound rate do you have? "))
print("Initial = $", round(invest,2), sep="")
print("Annual compound =", rate, "%", sep="")
rate = rate/100+1
years=0
print("")
while invest<total:
    invest=invest*rate
    years+=1
    print("Year", years)
    print("Total = $", round(invest,2))
    print("")

