#this code checks if you have entered a palindrome

#input string
string = str(input("Enter a string"))

#reverse string
stringreversed = string[::-1]

#check if the string is a palindrome
if string == stringreversed:
    print("This is a palindrome.")
else:
    print("Not a palindrome.")
#endif