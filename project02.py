#Dictionary

#1. Interface
#2. I need to develop the ord matching
#3. Modify my program

#How to get data????
#Using data.json file --> They provide it

import json
from difflib import get_close_matches

data = json.load(open("data.json"))
#print(data)

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    if word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())[0]) > 0:
        print('Did you mean %s instead ' %get_close_matches(word, data.keys())[0])
        decide = input('Press y for yes or press n for no : ')
        if decide == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == 'n':
            return 'You are enter the wrong word, plrase check it again...'
        else:
            return 'You have entered wrong input, pleas input y or n'
    else:
        #print('You are enter the wrong word, plrase check it again...')
        #x = 'You are enter the wrong word, plrase check it again...'
        return 'You are enter the wrong word, plrase check it again...'

word = input('Enter the word you want to search : ')
output = translate(word)
#print(output)

#print the output line by line
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
