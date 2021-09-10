#this code finds the number of words in a sentence

#input sentence
sentence = str(input("Type a random sentence"))

#finds the number of searches
numofsearch = len(sentence)

#searches for ' ' (space)
i = 0
count = 0
for i in range(0, numofsearch):
    if sentence[i] == " ":
        count += 1
    #endif
#next
print(count + 1)
