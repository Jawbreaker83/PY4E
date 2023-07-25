total = 0
count = 0
while True: #if reading a file this would be a for loop, since it is user input use a while loop;
	inp = input('Enter a Number: ')
	if inp == 'done' : break
	value = float(inp)
	total = total + value
	count = count + 1

average = total / count
print('Average:', average)