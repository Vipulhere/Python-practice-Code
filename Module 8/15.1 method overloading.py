class cars():
    def __init__(self):
        self.name="BMW"

    def show_detail(self):
        print(self.name)

class BMW(cars):
    def __init__(self):
        self.name="This is BMW Name"

    def show_detail(self):
        print(self.name)

c=cars()
c1=BMW()
c1.show_detail()
c.show_detail()