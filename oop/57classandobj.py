class Person():
    name = "Varun"
    occupation = "Software Developer"
    networth = 10000

    def info(self):
        print(f"hello {self.name} ur occupation is {self.occupation}")


a= Person()
print(a.name)


b=Person()
b.name="Ridam"
b.occupation="HR"
b.networth=100

b.info()