class parent:
    parentname=""
    childname=""
    def showparent(self):
        print(self.parentname)

class son(parent):
    def showchild(self):
        print(self.childname)
class daughter(parent):
    def showchild(self):
        print(self.childname)
s=son()
s.parentname="BoB"
s.childname="david"
s.showparent()
s.showchild()
d=daughter()
d.childname="alexa"
d.parentname="BOB"
d.showparent()
d.showchild()