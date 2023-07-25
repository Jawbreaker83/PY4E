#Not all regular expression repeat codes are greedy; if you add a ? character, the + and the * chill out a bit.

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)#The ? mark prefers the shortest 
print(y)