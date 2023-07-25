#If we could construct a list of tuples of the form (value,key) we could sort
#by value; we do this with a for loop that creates a list of tuples;

c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
	tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)#additional parameter added to sort from high to low
print(tmp)