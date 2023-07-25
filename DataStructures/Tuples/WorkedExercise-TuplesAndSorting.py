fname = input('Enter File: ')
if len(fname) < 1:fname='clowntext.txt'
hand = open(fname)

di=dict()
for lin in hand:
	lin = lin.rstrip()
	wds = lin.split()
	for w in wds:
		di[w] = di.get(w,0) +1

largest = -1
theword = None
for k,v in di.items():
	if v > largest:
		largest = v
		theword = k

#print(di)

#x = sorted(di.items())
#print(x)

tmp = list()
for k,v in di.items():
	#print(k,v)
	newt = (v,k)
	tmp.append(newt)

#print('Flipped', tmp)

tmp=sorted(tmp, reverse=True)#The reverse will sort highest to lowest
#print('Sorted',tmp[:5])

for v,k in tmp[:5]:
	print(k,v)