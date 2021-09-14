#This code does Rock Paper Scissors in one line

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
use = int(input("Enter your choice as '0 (Rock)', '1 (Paper)' and '2 (Scissors)'"))

#the core algorithm
result=(3+com-use)%3

#result analysis
if result == 0:
    print("Draw")
elif result == 1:
    print("Computer wins")
elif result == 2:
    print("You win")
#endif