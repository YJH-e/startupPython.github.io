#separating the digits of a number
num = int(input("Please enter a three digit number"))
hundred = num//100
ten = (num - 100*hundred)//10
unit = num - 100*hundred - 10*ten
print(hundred, "hundreds,", ten, "tens", unit, "units")

### ACS - that's good however there are not enough comkments. It is unclear what your algorithm is - 