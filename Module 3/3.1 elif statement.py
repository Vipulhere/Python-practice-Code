x=2
if x==1:
    print("X is 1")
elif x==4:
    print("X is 4")

elif x==5:
    print("X is 5")
else:
    print("X is something Else")
print("=====================")
price=60
qty=10
amount=price*qty

if amount>500:
    print("15% discount is given")
    discount=amount*15/100
    amount=amount-discount
    print("this payble amount is ",amount)
elif amount>400:
    print("10 % discount id given")
    discount = amount * 10 / 100
    amount = amount - discount
    print("this payble amount is ", amount)

else:
    print("No discount Given")