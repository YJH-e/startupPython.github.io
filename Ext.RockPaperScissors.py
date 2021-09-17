#this code plays rock paper scissors with you

#import random number generator
import random
comrandom = (random.randrange(0, 3))

#computer's choice
if comrandom == 0:
    com = "R"
elif comrandom == 1:
    com = "P"
elif comrandom == 2:
    com = "S"
#endif

#user's choice (to upper case to align with computer's choice)
use = str(input("Enter your choice as 'R', 'P' and 'S'"))

#compare results
if com == use:
    print("Draw")
else:
    if com == "R":
        if use == "P":
            print("User wins")
        elif use == "S":
            print("Computer wins")
        #endif
    elif com == "P":
        if use == "R":
            print("Computer wins")
        elif use == "S":
            print("User wins")
        #endif
    elif com == "S":
        if use == "R":
            print("User wins")
        elif use == "P":
            print("Computer wins")
        #endif
    #endif
#endif