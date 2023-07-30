#The items() method in dicationaries returns a list of (key, value) tuples;

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
	print(k,v)

tups = d.items()
print(tups)