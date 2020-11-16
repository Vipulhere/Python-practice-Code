#a=10
#b=15
#if b<a:
    #print("B is greater then A")
#else:
 #   print

price=15
qty=20
amount=price*qty
if amount<100:
    print("15% discount")
    discount=amount*15/100
    amount=amount-discount
    print("amount payble",amount)
else:
    print("5% discount ")
    discount=amount*5/100
    amount=amount-discount
    print("amount payble",amount)