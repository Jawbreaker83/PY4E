#Paranthesis are not part of the match - but they tell where to start and stop what string to extract


import re

x = ('From Stephen.Marquard@uct.ac.za Sat Jan 5 09:14:16 2008')
y = re.findall('\S+@\S+', x)
print(y)
#Start extracting after the space;
y = re.findall('^From (\S+@\S+)', x)
print(y)