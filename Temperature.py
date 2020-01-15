type=input("Is the temperature in celsius or in fahrenheit? (C/F) ").lower()
temp=float(input("What temperature do you need to convert? "))
if type=="c":
    newtemp=temp*1.8+32
    print("Your original temperature was ", temp, "degrees celsius.",sep="")
    print("Your temperature in fahrenheit is ", round(newtemp,2), " degrees fahrenheit.",sep="")
elif type=="f":
    newtemp=(temp-32)/1.8
    print("Your original temperature was ", temp, " degrees fahrenheit.",sep="")
    print("Your temperature in fahrenheit is ", round(newtemp,2), " degrees celsius.",sep="")