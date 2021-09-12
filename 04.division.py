#a division code that outputs the whole number division and reminder

#input the integer and divisor
divident = int(input("Enter a whole integer"))
divisor = float(input("Enter a divisor"))

#whole number division
#displaying no decimals using integer function
print(int(divident // divisor))

#reminder number division
#displaying no decimals using round function
print(round(divident % divisor))

## GACS - ood. Works well. Is it posisble to output whole numbers not ones to 1 decimla place?
