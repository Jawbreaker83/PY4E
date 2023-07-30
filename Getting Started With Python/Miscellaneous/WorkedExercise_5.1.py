num = 0
tot = 0.0
while True :
	sval = input('Enter a number: ')
	if sval == 'Done' : 
		break #If I am done then break;
	try: #But if bad data is entered other than a number than print a message out and then continue back to the top;
		fval = float(sval)
	except:
		print('Invalid Input')
		continue
	fval = float(sval)
	#print(fval)
	num = num +1
	tot = tot + fval

#print('All Done')
print(tot, num, tot/num)
