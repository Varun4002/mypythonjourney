x = 6

match x:
    case 0:
        print("the number is zero")

    case 4 if x%2==0:
        print("the number is even")

    case 6 if x % 2 == 0:
        print("the number is even")

    case _ if x%2!=0:
        print("its odd")
