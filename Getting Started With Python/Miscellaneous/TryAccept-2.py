#Way to eliminate or catch a traceback.  Code that python will execute if something goes wrong.  If things work out do this, if not do that type of conditional logic.
rawstr=input('Enter a Number:')
try:
	ival=int(rawstr)
except:
	ival=-1

if ival >0:
	print('Nice Work')
else:
	print('Not a number')
