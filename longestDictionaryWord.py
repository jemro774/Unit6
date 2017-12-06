#Jack Robey
#12/6/17
#longestDictionaryWord.py - prints out the longest word in the dictionary file

dictionary = open('engmix.txt')

longest = ''
for word in dictionary:
    if len(word) > len(longest):
        longest = word
print('The longest word in the dictionary is', longest)