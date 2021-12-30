#this code performs Caesar Cypher

#enter plain text
originalplain = str(input("Enter the message you want to encrypt"))
plainl = len(originalplain)

#make plain text lower case
plain = originalplain.lower()

#choose encryption
shift = int(input("How many letters to the right would you like to shift your text?"))

#encrypt
i = 0
cypher = ""
for i in range(0, plainl):
    char = plain[i]
    if char != " ":
        charASCII = ord(char) #find the ASCII value of a character
        newcharASCII = charASCII + shift
        #a -> z and z -> a with intensive maths
        if newcharASCII < 97:
            newcharASCII = 122 - (96 - newcharASCII)
        elif newcharASCII > 122:
            newcharASCII = 96 + newcharASCII - 122
        #endif
        newchar = chr(newcharASCII) #find the character of an ASCII value
    cypher += newchar
#next
print(cypher)

## VCery good well done.