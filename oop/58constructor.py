class Person():

    def __init__(self,n,o):
        self.name = n
        self.occ = o

    def info(self):
        print(f"hi my name is {self.name} and my occupation is {self.occ}")


a= Person("Varun","Software Engineer")
a.info()


class Car:
    def __init__(self,model,year):
        self.model = model
        self.year = year

    def info(self):
        print(f"The car is {self.model} year {self.year}")

a = Car("Buggati",2021)
a.info()