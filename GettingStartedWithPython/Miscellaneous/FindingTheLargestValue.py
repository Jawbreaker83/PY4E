largest_so_far = -1
print('Before', largest_so_far) #Stuff we do before the loop;
for the_num in [9, 41, 12, 3, 74,15]: # stuff we do during the loop;
	if the_num > largest_so_far:
		largest_so_far = the_num
	print(largest_so_far, the_num)

print('After', largest_so_far)# stuff we do after the loop finishes;