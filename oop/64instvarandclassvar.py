class Car():

    wheels = 4      #class variable

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def info(self):
        print(f"the make of car is {self.make} the model is {self.model} and the year is {self.year} and the colour is {self.color}")



car1 = Car("Baleno","suv","2021","grey")
car1.wheels = 2         #this is instance variable
print(car1.wheels)

car1.info()