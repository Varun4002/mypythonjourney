class Employee:
    company = 'Apple'

    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    
    def changeCompany(cls,newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name="Varun"
e1.show()

e1.changeCompany("Tesla")
print(e1.company)