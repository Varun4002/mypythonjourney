#hybrid inhertance
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1,Derived2):
    pass

#Heirachial

class Organism:
    
    alive = True

class Animal(Organism):

    def eat(self):
        print("this animal is eating")

class Budgie(Animal):

    def chirps(self):
        print("this Budgie is chirping")



budgie = Budgie()
print(budgie.alive)