#this code calculates the seconds in the time entered

#enter time
hour = int(input("Enter hours"))
min = int(input("Enter minutes"))
sec = int(input("Enter seconds"))

#calculates total time
total = hour * 3600 + min * 60 + sec

#outputs result
print(total)