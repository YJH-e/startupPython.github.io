#option between 1 to 3
option = int(input("Enter a number between 1 and 3"))

while option < 0 or option > 3:
    option = int(input("Enter a number between 1 and 3 again"))

#endwhile

#display option
print("You have selected option number ", option)


## ACS Very good and fits the brief. Later on we will do some work on validation checks. It crashes if I put in the letter a for example!