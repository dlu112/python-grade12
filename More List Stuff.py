list = []
word = input("Type something: ")
for char in word:
    list.append(ord(char))
print("In ASCII, '",word, "' is:", list)
print("")

print("Decoding")
text = ""
for x in list:
    text = text + chr(x)
print(text)