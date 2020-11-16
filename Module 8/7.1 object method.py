class car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def car_detail(self):
        print("Name of car",self.name)
        print("Color of car",self.color)

c=car("ford","white")
c.car_detail()