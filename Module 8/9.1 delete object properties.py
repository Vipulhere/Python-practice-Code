class car:
    def __init__(self,name,color,model):
        self.name=name
        self.color=color
        self.model=model

c1=car("ford","white",2020)
c2=car("toyota","black",2015)
c4=car("BMW","green",2019)
print(c1.name,c1.color,c1.model)
print(c2.name,c2.color,c2.model)
print(c4.name,c4.color,c4.model)
del c1.name
del c2
print(c1.color,c1.model)
print(c2)
