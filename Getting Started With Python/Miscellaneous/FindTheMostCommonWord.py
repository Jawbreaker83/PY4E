# Find the Most Common Word
bigcount=None
bigword=None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword=word
		bigcount=count
		