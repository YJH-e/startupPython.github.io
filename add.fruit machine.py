#this code simulate a fruit machine

#initialise the credit of the player in pence
credit = 100
print("You have £", credit/100)

#declare the list for storing results
result=[]

#import random number generator
import random

#start a go
credit = credit - 20
counter = 0
numskull = 0 #check if two or more skulls appear
numbell = 0 #check if three bells appear
while counter < 3:
    result[counter] = (random.randrange(0, 6))
    # 0 is Cherry
    # 1 is Bell
    # 2 is Lemon
    # 3 is Orange
    # 4 is Star
    # 5 is Skull
    if result[counter] == 5: #check if two or more skulls appear
        numskull += 1
    elif result[counter] == 1: #check if three bells appear
        numbell += 1
    #endif
    counter += 1
#endwhile

#analyse the results
#check if two or more skulls are present
if numskull >= 2:
    credit = credit - 100

#check if three bells are present
elif numbell == 3:
    credit = credit + 500

#check if all three symbols are the same
elif result[0] == result[1] and result[0] == result[1]:
    credit = credit + 100

#two the same symbol that are not skulls
elif result[0] == result[1] or result[0] == result[2] or result[1] == result[2]:
    credit = credit + 50
#endif

#display remaining credit
print("You now have £", credit/100)