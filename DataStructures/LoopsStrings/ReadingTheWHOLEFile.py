#Reading the whole file (newlines and all) into a single string;
fhand = open ('mbox-short.txt')
inp = fhand.read()
print(len(inp))
94626
print(inp[:20])
from stephen.marquar