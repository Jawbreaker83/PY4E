#Method for a running total of the items, in this case the running total of the numbers
#within the string is 154;
zork = 0
print("Beofre", zork)
for thing in [9, 41, 12, 3, 74, 15]:
	zork = zork + thing
	print(zork, thing)
print("After", zork)