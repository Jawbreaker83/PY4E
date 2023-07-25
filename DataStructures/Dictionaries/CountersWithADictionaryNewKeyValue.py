#When encountering a newe 2nd or later time that we have seen the key we simply add one to the 
#coun in the dicti key you need to add a new entry into the dictionary
# and if this is thonary under that key;

counts = dict() #step 1 creating a dictionary;
names = {'csev', 'cwen', 'zqian','cwen'} #Step 2 dictionary of the names;
for name in names: #The For loop with name as the iteration variable going through the loop;
	if name not in counts: #asking the question if the name we are looking at not in the dictionary then set the subcount to 1, getting things started.
		counts[name] = 1
	else: #if the name is in the dictionary this code will extract the current value and add 1 to it;
		counts[name] = counts[name] +1
print(counts)