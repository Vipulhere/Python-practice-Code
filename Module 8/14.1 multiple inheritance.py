class father:
    def __init__(self,fathername,fatherage):
        self.name=fathername
        self.age=fatherage
    def showname(self):
        print(self.name)
    def age(self):
        print(self.age)
class mother:
    def __init__(self,mothername):
        self.mothername=mothername
    def showmothername(self):
        return self.mothername

class son(father,mother):
    def __init__(self,name,age,mothername):
        father.__init__(self,name,age)
        mother.__init__(self,mothername)
s=son("David",50,"alexa")
s.showname()
print(s.showmothername())

