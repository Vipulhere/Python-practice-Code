try:
    text=input("Enter a value or something you like")
except EOFError:
    print("EOF Error")
except KeyboardInterrupt:
    print("You cancelled the operation")
else:
    print("you enterd".format(text))
