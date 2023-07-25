#You can refine the match for re.find() and separetely determine which portion of the match is to be extracted by using paratheses.

import re

x = ('From Stephen.Marquard@uct.ac.za Sat Jan 5 09:14:16 2008')
y = re.findall('\S+@\S+', x)
print(y)