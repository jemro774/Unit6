#Jack Robey
#12/11/17
#warmup16.py - finds all the words in the dictionary that start with your first initial and end with your last initial

dictionary = open('engmix.txt')

for word in dictionary:
    if len(word) > 0:
        if word.strip()[0] == 'j' and word.strip()[-1] == 'r':
            print(word.strip())