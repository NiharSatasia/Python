'''
Created on Apr 21, 2021

@author: niharsatasia

'''

import re

# Find a string that includes an "a" followed by 0 or more "b"s

def text_match(text):

        patterns = "ab*?"

        if re.search(patterns,  text):

                return 'Found a match!'

        else:

                return('Not matched!')

 

print(text_match("ac"))

print(text_match("abc"))

print(text_match("abbc"))

print(text_match("bbc"))

