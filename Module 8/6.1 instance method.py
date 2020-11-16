class car:
    """THis is a instance method """
    model=2020
    def cartype(self):
        print("sports cars")

c=car()
print(c.model)
c.cartype()
print(car.__doc__)
