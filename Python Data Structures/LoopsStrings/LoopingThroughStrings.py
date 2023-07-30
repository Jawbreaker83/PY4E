# A loop that goes through each of the letters within a string;
fruit = 'banana'
index = 0 #iteration variable;
while index < len(fruit):
	x = fruit [index] #Looks up the letter at position 0, 1, 2, etc and places the letter into the variable x
	print (index, x)
	index = index + 1 