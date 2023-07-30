#You take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary;
#first sort the dictionary by the key using the items() method
#and sorted() function; loop through the dictionary in KEY ORDER NOT VALUE ORDER:

d = {'a':10, 'b':1, 'c':22}
t=sorted(d.items())
print(t)
for k,v in sorted(d.items()):
	print(k,v)