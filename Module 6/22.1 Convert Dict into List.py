dict={
    "BMW":"2012",
    "FORD":"2014"
}
lst=[]
for a in dict:
    b=(a,dict[a])
    lst.append(b)
print(lst)