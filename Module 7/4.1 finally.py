a=15
try:
    print(a)
except:
    print("Something is wrong")
finally:
    print("try Except is Finished right here")

try:
    b=open("txt.txt")
finally:
    b.close()