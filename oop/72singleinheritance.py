class Animal:
    def eat(self):
        print("animal eats")

    
class Bird(Animal):
    def fly(self):
        print("this bird can fly")


bird = Bird()
bird.eat()