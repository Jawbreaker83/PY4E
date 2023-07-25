#The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible
#string.  Both the asterisk and the plus push as far outward as they can.

import re
x= 'From: Using the : character'
#^ = 1st character is an 'F'; the . is any character and the + is one or more times and then a start with a colon 
y = re.findall('^F.+:', x)
print(y)


