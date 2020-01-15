# Question 1, Newspaper Delivery Program #


print("Types of subscriptions")
print("Weekdays (Monday to Friday), $13.00 for 13 weeks.")
print("Weekends (Saturday and Sunday), $6.00 for 13 weeks")
print("Full Weeks (Monday to Sunday), $14.00 for 13 weeks")
subtype=input("What type of subscription do you want? ")


while True:
    if subtype.lower() == "weekdays":
        cost = 13.00
        break
    elif subtype.lower() == "weekends":
        cost = 6.00
        break
    elif subtype.lower() == "full weeks":
        cost = 14.00
        break
    else:
        print("Subscription type not valid, please try again")
        subtype = input("What type of subscription do you want? ")
print("Your cost will be $",cost,"0 for this 13 week subscription.", sep="")

# The costs weren't being rounded properly, hence the extra zero #


# Question 2, ASCII Conversion #

ASCIIList = [77,111,115,116,32,116,105,109,101,115,32,121,111,117,114,32,99,111,109,112,117,116,101,114,32,105,115,32,110,111,116,32,114,101,115,112,111,110,100,105,110,103,32,97,115,32,121,111,117,32,101,120,112,101,99,116,101,100,32,45,32,102,105,114,115,116,32,116,114,121,32,116,111,32,102,105,110,100,32,111,117,116,32,105,102,32,116,104,101,32,226,128,156,69,82,82,79,82,226,128,157,32,105,115,32,110,111,116,32,115,105,116,116,105,110,103,32,114,105,103,104,116,32,110,101,120,116,32,116,111, 32,116,104,101,32,99,111,109,112,117,116,101,114,46]
print("")
print("Decoding")
text = ""
for x in ASCIIList:
    text += chr(int(x))
print(text)