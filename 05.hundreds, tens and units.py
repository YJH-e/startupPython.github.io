#separating the digits of a number

#input number
num = int(input("Please enter a three digit number"))

#get hundreds
hundred = num//100

#get tens
ten = (num - 100*hundred)//10

#get units
unit = num - 100*hundred - 10*ten
<<<<<<< HEAD

#display results
print(hundred, "hundreds,", ten, "tens", unit, "units")
=======
print(hundred, "hundreds,", ten, "tens", unit, "units")

### ACS - that's good however there are not enough comkments. It is unclear what your algorithm is - 
>>>>>>> ccbf6f6f50bc9b0b1856bdd627f49a55ec8a1e14
