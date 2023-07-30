fname = input('Enter a File Name: ')
han = open('mbox-short.txt') #Opens a file;

for line in han: #loop through the file;
	line = line.rstrip() #Throw away the white space to the right of the line;
	wds = line.split() #Splits into words;
	if len(wds) < 3: #A Guardian of sorts; checks the line to see that there are at least 3 words;
		continue
	if wds [0] != 'From': #Checks to see if the 2st word in the line starts with from, if is not skip and read the next line;
		continue
	print(wds[2])


