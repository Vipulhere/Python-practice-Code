class animal:
    def noise(self):
        raise NotImplementedError
class cat(animal):
    def noise(self):
        print("Meoow")
class dog(animal):
    def noise(self):
        print("woof")
a=cat()
a.noise()
a=dog()
a.noise()