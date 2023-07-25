#If you just want to search and know if a value was founds, us a variable that stats at FALSE and is set to TRUE as soon as you locate what you are looking for;
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
	if value == 3 :
		found = True
	print(found, value)
print('After', found)
