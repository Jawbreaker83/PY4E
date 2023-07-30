#A method not for counting the number of items within a loop, in this case there are six items in the loop;
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
	zork = zork + 1
	print(zork, thing)
print("After", zork)