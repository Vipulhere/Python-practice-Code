class car:
    name="Ford"
    color="white"
    model=2020
    def display1(self):
        print(self.name)
        print(self.color)
        print(self.model)
c=car()
print (getattr(c,"name"))
print (hasattr(c,"name"))
print (setattr(c,"model",2015))
print(c.model)
print(getattr(c,"color"))
print(delattr(c,"model"))
print(c.name,c.model,c.color)