#List comprehension creates a dynamic list.  In this case, we
#make a list of reversed tuples and then sort it;

fhand = open('romeo.txt') #open file
counts = dict()#make dictionary
for line in fhand:#loop through all of the lines of the file
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1#Code to construct the histogram of counts

c = {'a':10, 'b': 1, 'c': 22}
#an expression of a list as an expression; for all create tuples that are v,k tupples, looping through all k,v items witnin the c dictionary
print(sorted([(v,k) for k,v in c.items()]))