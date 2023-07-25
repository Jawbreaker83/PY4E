#Way to eliminate or catch a traceback.  Code that python will execute if something goes wrong.  If things work out do this, if not do that type of conditional logic.
astr='Hello Bob'
try:
	istr=int(astr)
except:
	istr=-1

print('First', istr)

astr='123'
try:
	istr = int(astr)
except:
	istr = -1

print('Second', istr)

