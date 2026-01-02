User_Input = int(input("Enter a number: "))
if User_Input <=0:
    print("Enter a number greater than 0")
elif User_Input % 2 == 0:
    print(f"{User_Input} is Even")
else:
    print(f"{User_Input} is Odd")