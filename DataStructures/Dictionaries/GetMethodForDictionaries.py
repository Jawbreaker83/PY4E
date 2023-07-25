#The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key
#is not there is so common that there is a method called get() that does this 
#for us; 

if name in counts:
	x=counts[name]
else: 
	x = 0

x = counts.get(name,0) #this code say go look up in counts using name as the key and 0 as the default (meaning the 
					#value you get back if the key does not exist)