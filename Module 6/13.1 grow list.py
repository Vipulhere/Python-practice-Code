import random
list=["python","php","java","c++"]
print(list)
random.shuffle(list,random.random)
print(list)

print("____________________")
list2=["canada","USA","UK","China"]
list3=["brazil","Germany"]
list4=list2+list3
mergedlist=[]
mergedlist.extend(list2)
mergedlist.extend(list3)
print(mergedlist)