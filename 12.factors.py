#this code finds all the factors of an integer

#import the math functions needed
from math import sqrt

#enter integer
iNum = int(input("Enter an integer"))

#find square root
endnum = sqrt(iNum)

#set up factor array/list
factors = []

#find factors
i=2
while i <= endnum:
    tempfactor = (iNum/i)
    if tempfactor - int(tempfactor) == 0:
        factors.append(i)
        factors.append(int(tempfactor))
    #endif
    i += 1
#endwhile

#print all factors using "sorted" which sorts all values from minimum to maximum
print(sorted(factors))
## ACS - That's good work 