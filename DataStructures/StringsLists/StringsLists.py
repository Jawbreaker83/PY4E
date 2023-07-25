#Split breaks a string into parts and produces a list of strings; think of these as words that can be accessed through all the words;
#The pattern for how to read a line, break it into pieces and then look at each word in the line, a split and then a for loop;

abc = 'With three words'
stuff = abc.split() #Basically takes a string and gives back a list;
print(stuff)
print(len(stuff))
print(stuff[0])

print(stuff)
for w in stuff: #The iteration variable is 'w' that will loop through the list
	print(w)