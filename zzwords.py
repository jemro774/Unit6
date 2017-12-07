#Jack Robey
#12/7/17
#zzwords.py - prints out all words that contain zz

dictionary = open('engmix.txt')

for word in dictionary:
    if 'zz' in word:
        print(word.strip())

