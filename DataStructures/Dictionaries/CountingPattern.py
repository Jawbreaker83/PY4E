#Will use a dictionary, use splits to get a list and then loop the list and do the historgram patter;
#The general pattern to count the words in a line of text is to 
#split the line into words, then loop through the words and use a dictionary
#to track the count of each word independently

counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words', words)

print('Counting...')
for word in words:
	counts[word] = counts.get(word,0) +1
print('Counts', counts)