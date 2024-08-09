class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

e = Employee("Varun",60000)
print(e.name)

string = "Varun-1200000"
e2= Employee.fromstr(string)
print(e2.name)