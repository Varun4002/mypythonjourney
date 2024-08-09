try:
    l=[1,5,7,9,11]
    i = int(input("enter the index "))
    print(l[i])

except:
    print("some error occoured")

finally:
    print("the execution is completed")