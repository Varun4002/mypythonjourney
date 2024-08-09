countries = ("India","Russia","USA","UKRAIN")

temp = list(countries)
temp.pop()
countries=tuple(temp)
print(countries)



collage_friends = ("rohit","rahul")
school_friends =("aman","rachit")
friends = collage_friends + school_friends
print(friends)

tup = (1,1,3,4,5,1,1,7,8,6,8,5,11,1,1,67)
print(tup.count(1))
print(tup.index(11))