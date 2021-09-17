#this code produces all combinations for a four digit PIN code
print("All possible combinations are listed below")
tries = 0
emptydigit = "0"

while tries < 100:
    combination = str(tries)
    digit = len(combination)
    
    #fill in the empty digits if a combination does not have 4 digits
    while digit < 2:
        combination = emptydigit + combination
    #endwhile
    #display combination
    print(combination)

    tries += 1
#endwhile