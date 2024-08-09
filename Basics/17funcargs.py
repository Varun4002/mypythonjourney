# def avg(a=9,b=7):                       #giving default value
#     print("the avg is ",(a+b)/2)
#
# avg()

# def name(fname="Cookie",mname="Oregiano",lname="Sharma"):
#     print("hello",fname,mname,lname)
#

def numbers(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    return sum

print(numbers(67,89,76,56))