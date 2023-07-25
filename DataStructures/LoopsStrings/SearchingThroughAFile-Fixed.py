#Strip whitespace from the right-hand side of the string using rstrip() from the string library; The newline is consdered 'whte space' and is stripped:
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip() #open a file, read through all of the lines, throw away the whitespace and then do something with the lines of code;
	if line.startswith('From'):
		print(line)