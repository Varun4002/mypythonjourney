marks = [3,5,6,"zero",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
marks.append(7)
print(marks)

if 6 in marks:
    print("Yes")
else:
    print("No")

print(marks[0:4:2])
print(marks)
print(marks[:-1])
print(marks[::])