a = int(input("enter a number between 6 and 10"))

if (a<6 or a>10):
    raise ValueError("value should be between 6 and 10")