#this code compares the value of two numbers and outputs them in numerical order from the highest to the lowest

#input number
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

#compares the size of the two numbers
if num1 < num2:
    print(num2, num1)
else:
    print(num1, num2)
#endif