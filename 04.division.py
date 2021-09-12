#a division code that outputs the whole number division and reminder

#input the integer and divisor
divident = int(input("Enter a whole integer"))
divisor = float(input("Enter a divisor"))

#whole number division
#displaying no decimals
print(int(divident // divisor))

#reminder number division
#displaying no decimals with another method
print(round(divident % divisor))