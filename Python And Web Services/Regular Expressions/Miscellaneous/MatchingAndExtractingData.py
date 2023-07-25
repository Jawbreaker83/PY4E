#re.search90 returns a T\F depending on whether the string matches the regular expression.
#If we actually want the matching strings to be extracted, we use 
# re.findall()

import re 
x ='My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x ) #The + indicates one or more digits; runs all the way through the text you have requested and returns a list of matches.
print(y) #returns three strings
y=re.findall('[AEIOU]+',x)
print(y)