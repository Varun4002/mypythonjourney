class Prey:
    def flee(self):
        print("this animal flees")

class Predator:
    def hunt(self):
        print("this animal is hunting")


class Rabbit(Prey):
    def hop(self):
        print("this animal hops")

class Fish(Prey,Predator):
    def swim(self):
        print("this animal swims")

    
rabbit =Rabbit()
rabbit.flee()

fish = Fish()
fish.flee()
fish.hunt()