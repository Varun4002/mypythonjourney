class rectangle:
     def __init__(self,width,length):
        self.length = length
        self.width = width

class Square(rectangle):
    def __init__(self,width,length):
        super().__init__(length,width)

    def area(self):
        return self.width*self.length

class Cube(rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height


square = Square(5,5)
square.area()