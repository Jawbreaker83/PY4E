#Using re.search() Like find()

#hand = open('mbox-short.txt')
#for line in hand:
#	line = line.rstrip()
#	if line.find('From:') >= 0:
#		print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	#import of the regular expression libary; open a file, loop through the file; re.search is a object oriented pattern using variable name method; 
	if re.search('From:', line):
		print(line)
		