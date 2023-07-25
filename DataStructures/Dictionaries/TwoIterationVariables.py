#Loop through the key-value pairs in a dictionary using two iteratation variables.  Each
#iteration, the first variable is the key and the second variable is the corresponding key.

jjj = {'chuck': 1, 'fred': 42, 'jan' : 100}
for key,value in jjj.items(): #two iterattion variables used to loop thru the dictionay all key value pairs
	print(key,value)