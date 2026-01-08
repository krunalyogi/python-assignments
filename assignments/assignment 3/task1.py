def factorial(n):
    fact=1
    while n>1:
        fact*=n
        n-=1
    return fact
num=int(input("enter the number: "))
print(f"factorial of {num} is: {factorial(num)}")