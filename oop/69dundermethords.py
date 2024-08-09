class Employee:
    name = "Varun"
    def __len__(self):
        for c in self.name:
            i=i+1
            return i
        
e=Employee()
print(e.name)
print(len(e))