#Jack Robey 
#12/13/17 
#quiz6.py 

dictionary = open('engmix.txt') 
for word in dictionary: 
    if word.count('c') == 3 and word.count('p') == 2: 
        print(word.strip())
