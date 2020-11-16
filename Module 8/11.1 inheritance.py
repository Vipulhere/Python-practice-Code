#parent class
class parent:
    parentname=""
    childname=""
    def show_parent(self):
        print(self.parentname)

#this is child class which is inherites from parent
class Child(parent):
    def show_child(self):
        print(self.childname)
#this object of child class
c=Child()
c.parentname="BOB"
c.childname="David"
c.show_parent()
c.show_child()

print("___________________")
class car:
    def __init__(self,name="ford",model=2015):
        self.name=name
        self.model=model
    def sport(self):
        print("this is sport car")
class sportcar(car):
    pass
c=sportcar("sportcar")
print(c.name)
print(c.model)
c.sport()
