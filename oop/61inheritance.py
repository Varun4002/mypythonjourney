class Programmer:               #parent class
    
    def ide(self):
        print("this programer uses Vscode")


class webdeveloper(Programmer):         #child class

    def language(self):
        print("this programmer uses html")


class javadeveloper(Programmer):        #child class

    def language(self):
        print("this programer uses Java")


a = webdeveloper()
a.ide()

b= javadeveloper()
b.language()
b.ide()