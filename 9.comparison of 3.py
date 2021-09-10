#this code compares the value of three numbers and outputs them in numerical order from the highest to the lowest

#input numbers
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))

#compares the size of the two numbers
if num1 <= num2:
    if num2 <= num3:
        print(num3, num2, num1)
    elif num1 <= num3:
        print(num2, num3, num1)
    else:
        print(num2, num1, num3)
    #endif
else:
    if num1 <= num3:
        print(num3, num1, num2)
    elif num2 <= num3:
        print(num1, num3, num2)
    else:
        print(num1, num2, num3)
    #endif
#endif