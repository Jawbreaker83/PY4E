#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

fname = input('Enter a File Name: ')
fhand = open('mbox-short.txt') #open the file;
for line in fhand: #loop through the file;
	line = line.rstrip() #strip the white space off of the right side of the file;
	if not line.startswith('From') : continue #Check to see if it starts with From if not continue;
	words = line.split()
	print(words[1]) #As soon as we see the word from we split the code and pull out the 2nd word sub 2 will always be the day of the week within the line above