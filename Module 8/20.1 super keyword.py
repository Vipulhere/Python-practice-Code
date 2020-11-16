class A:
    def method1(self):
        print("I am calling parent class")

class B(A):
    def method1(self):
        print("Calling the child class")
        super().method1()
c=B()
c.method1()