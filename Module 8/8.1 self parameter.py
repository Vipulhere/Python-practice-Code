class car:
    def __init__(selfcar,name,color):
        selfcar.name=name
        selfcar.color=color

    def detail_car(selfcar):
        print("Car Name",selfcar.name)
        print("car Color",selfcar.color)
c=car("ford","black")
c.detail_car()