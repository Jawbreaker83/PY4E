# Count Word Frequency
counts=dict()
for line in handle:
	words=line.split()
	for word in words:
		counts(word)=counts.get(word,0)+1