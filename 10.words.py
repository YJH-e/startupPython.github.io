#this code finds the number of words in a sentence

#input sentence
sentence = str(input("Type a random sentence"))

#find the number of spaces, which is one less than the number of words
print(sentence.count(' ') + 1)

