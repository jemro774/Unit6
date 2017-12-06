#Jack Robey
#12/6/17
#fileDemo.py

dictionary = open('engmix.txt')

for word in dictionary:
    if 'jack' in word:
        print(word.strip())
