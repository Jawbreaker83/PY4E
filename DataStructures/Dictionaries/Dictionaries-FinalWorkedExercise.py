



fname = input('Enter File: ')
#code inserted allowing you to just hit enter without having to enter the filename;
if len(fname) < 1 : fname = 'clowntext.txt' 
hand = open(fname)

di = dict()#di is the user chosen variable and dict is a type of python dictionary;
for lin in hand:
	lin = lin.rstrip()
	#code inserted to test the file is opened correctly and you can print the line with the strip;
	#print(lin)
	wds = lin.split()
	#code inserted to further test the line is split
	#print(wds)
	for w in wds: #wds is a python list created in line 14;
		
		#these lines of code can be consolidated;
		#if w in di:
		#	di[w]=di[w] +1
		#	print('**Existing**')
		#else:
		#	di[w]= 1
		#	print('**New**')
		
		#Code below says get the old value from this key or 0 and then add 1 to it;
		#idiom, retrieve, create and update counter within 1 line of code;
		di[w] = di.get(w,0) +1
		#print(w,'new', di[w])

#print(di)
#The next step after printing out the dictionary is to find the most common word;
largest = -1
theword = None
for k,v in di.items(): #items is a method inside of all dictionaries that will return the key value pairs
	print(k,v)
	if v > largest:
		largest = v
		theword = k
print('Done',theword, largest)




	