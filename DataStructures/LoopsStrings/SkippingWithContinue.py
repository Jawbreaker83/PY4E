#Skip a line by using the continue statement;
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From:'): #if the line does not start with 'From' continue, skip everything that does not start with 'From;'
		continue
	print(line)