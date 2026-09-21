textEntered = ""
stringBuilder = ""
while textEntered != "quit":
    textEntered = input("Enter in a string enter quit to exit loop  >")
    if textEntered != "quit":
        stringBuilder += textEntered + ""
print(stringBuilder)
