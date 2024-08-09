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