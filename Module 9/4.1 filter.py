def abc(a):
    if a>5:
        return a
c=filter(abc,(1,2,4,9))
print(list(c))