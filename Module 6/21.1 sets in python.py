s={2,3,4,5,6,7,8,9}
print(s)
s1=set([1,2,3,4,5,6,7,8,9,9,9,9])
print(len(s1))
s2=set()
s2.add("a")
s2.add("b")
s2.add("c")
s2.add("d")
s2.add("e")
s2.add("e")
s2.add("e")

print(s2)
s3={"d","h","y"}
s2.update(s3)
print(s2)