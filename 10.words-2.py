#this code finds the number of words in a sentence

#input sentence
sentence = str(input("Type a random sentence"))

#find the number of words in the sentence inputted
words = 0
wordflag = False

#check every character and space in the sentence
index = len(sentence)
counter = 0
while counter < index:
    if sentence(counter) != " ":
        wordflag = True
    


#endwhile