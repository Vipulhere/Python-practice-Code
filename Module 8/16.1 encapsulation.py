class encapsulation:
    __name=None

    def __init__(self,name):
        self.__name=name
    def getname(self):
        return self.__name
e=encapsulation("Encapsulation")
print(e.getname())

print("________________")
class car(object):
    def __init__(self,name="BMw",year=2020,mileage="250",color="white"):
        self.__name=name
        self.__year=year
        self.__mileage=mileage
        self.__color=color

    def cardetail(self,speed):
        print("your car spreed is %s" %(self.__name,speed))
    def speeds(self,speed):
        print("meter speed is  %s"%speed)
c=car()
print(car.__name)
