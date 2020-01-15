#Question 2#
print ("Enter the amount spent last month on the following items:")
food = input("Food: $")
clothes = input("Clothing: $")
entertain = input("Entertainment: $")
rent = input("Rent: $")
total = float(food)+float(clothes)+float(entertain)+float(rent)
food = (float(food)/total)*100
clothes = (float(clothes)/total)*100
entertain = (float(entertain)/total)*100
rent = (float(rent)/total)*100
print ("In total you spent $", round(total,2)," on these items last month.", sep="")
print ("")
print ("Category Budget")
print ("Food ", round(food, 2),"%", sep="")
print ("Clothing ", round(clothes, 2),"%", sep="")
print ("Entertainment ", round(entertain, 2),"%", sep="")
print ("Rent ", round(rent, 2),"%", sep="")