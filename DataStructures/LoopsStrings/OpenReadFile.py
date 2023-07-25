fh = open('words.txt')

for lx in fh:
	ly = lx.strip()#throws away non-printing characters at the end of each line; upper is a method with the string variable in this case lx;
	print(ly)