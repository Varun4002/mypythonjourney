a = input("pls enter a number")

try:
    for i in range(1,11):
        print(f"{int(a)}X{i}={i*int(a)}")

except IndexError:
    print("Index error is present")

except IndexError:
    print("index errors")