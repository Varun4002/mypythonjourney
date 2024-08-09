#factorial = 7! =7x6x5x4x3x2x1

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        ans=n*factorial(n-1)

    return ans

print(factorial(5))