#this code produces all combinations for a four digit PIN code
print("All possible combinations are listed below")
tries = 0

#print out all combinations in order of values from smallest to largest
while tries < 10000:
    combination = str(tries)
    digit = len(combination)
    
    #fill in the empty digits if a combination does not have 4 digits
    if digit == 4:
        print(combination)
    elif digit == 3:
        print("0" + combination) # using '+' leaves no space between the two elements being added, or concatinated; while using ',' will leave a space
    elif digit == 2:
        print("00" + combination)
    elif digit == 1:
        print("000" + combination)
    tries += 1
#endwhile