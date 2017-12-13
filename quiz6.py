#Jack Robey 
#12/13/17 
#quiz6.py

dictionary = open('engmix.txt') #Opening the file


'''for word in dictionary: #Program #1 
    if word.count('c') == 3 and word.count('p') == 2: 
        print(word.strip())'''


'''dictionaryL = [] #Program #2

for word in dictionary:
    if len(word) > 0:
        if word.strip()[0] == 'r':
            dictionaryL.append(word.strip())

print(len(dictionaryL))'''


'''num = int(input('Enter a number: ')) #Program #3

dictionaryL = []

for word in dictionary:
    if len(word) == num:
        dictionaryL.append(word.strip())

print(dictionaryL[0])'''


'''dictionaryL = [] #Program #5

for word in dictionary:
    dictionaryL.append(word.strip())

print(dictionaryL[len(dictionaryL)/2])'''
