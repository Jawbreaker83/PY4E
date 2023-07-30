

fhand = open('romeo.txt') #open file
counts = dict()#make dictionary
for line in fhand:#loop through all of the lines of the file
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1

lst = list()
for key, value in counts.items():#
	newtup = (value,key)
	lst.append(newtup)

lst = sorted(lst, reverse=True)

for value, key in lst[:10]:
	print(key,value)