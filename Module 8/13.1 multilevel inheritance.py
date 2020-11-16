class family:
    def showfamily(self):
        print("This is family of 3 people")
class father(family):
    def fathername(self):
        print("father name is bob")
class son(father):
    def sonname(self):
        print("son name is david")
f=son()
f.fathername()
f.showfamily()
f.sonname()