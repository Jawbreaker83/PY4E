#Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again.

import re

line = ('From Stephen.Marquard@uct.ac.za Sat Jan 5 09:14:16 2008')

words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
