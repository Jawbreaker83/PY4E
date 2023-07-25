Name=input('Enter File:')
Handle=open(name,'r')
Counts=dict()

For line in handle:
	Words=line.split()
	For word in words:
		counts[word]=counts.get(word,0)+1
		
Bigcount=None
Bigword=None
For word, count in list(counts.items()):
	If bigcount is None or count>bigcount:
		Bigword=word

Print(bigword,bigcount)
