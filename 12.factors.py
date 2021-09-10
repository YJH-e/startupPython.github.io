#this code finds all the factors of an integer

#import the math functions needed
from math import sqrt

#enter integer
num = int(input("Enter an integer"))

#find square root
endnum = sqrt(num)

#set up factor array/list
factors = []

#find factors
i=2
while i <= endnum:
    tempfactor = num/i
    if tempfactor - int(tempfactor) == 0:
        factors.append(i)
        factors.append(tempfactor)
    #endif
    i += 1
#endwhile

#print all factors
print(factors)