#separating the digits of a number

#input number
num = int(input("Please enter a three digit number"))

#get hundreds
hundred = num//100

#get tens
ten = (num - 100*hundred)//10

#get units
unit = num - 100*hundred - 10*ten

#display results
print(hundred, "hundreds,", ten, "tens", unit, "units")