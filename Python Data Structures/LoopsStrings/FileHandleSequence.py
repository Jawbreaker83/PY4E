#File handle as a sequence.  A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence.  We can use the for statement to iterate through a sequence; remember a sequence is an ordered set;
xfile = open('mbox.txt')
for cheese in xfile: #treat a file handle as a sequence of lines and allow us to iterate through it automatically using the for loop;
	print (cheese)
