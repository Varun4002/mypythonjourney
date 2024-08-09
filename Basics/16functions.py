# a block of code that gets exexuted when its called
#helps reduce lines in code
#normal way
# a= 9
# b=8
# gmean=(a*b)/(a+b)
# print(gmean)
#
# def gmean(a,b):
#     return (a*b)/(a+b)
#
# print(gmean(9,8))


#isgreater
def isgreater(a,b):
    if a>b:
        print(a," is greater")
    elif a<b:
        print(b,"is greater")
    else:
        print(a," ",b," both are equal")

isgreater(56,79)