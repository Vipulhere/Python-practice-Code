number=12
i=0
val1=0
val2=1
while(i<number):
    if(i<=1):
        next=i
    else:
        next=val1+val2
        val1=val2
        val2=next

    print(next)
    i=i+1
