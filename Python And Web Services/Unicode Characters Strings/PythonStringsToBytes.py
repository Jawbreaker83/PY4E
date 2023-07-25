#In Python 3, all strings internally are UNICODE; working with string variables in Python programs and reading
#data from files usually 'just works'; When we talk to a network resource using sockets or talk to a database we have to encode and 
#decode data (usually to UTF-8)
#When talking to an external resource like a network socket we sends bytes, so we need to encode
#Python 3 strings into a give character encoding; when reading data from an external resource
#we must decode it based on the character set so it is properly represented in Python 3 as a string


While True:
	data = mysock.recv(512) #Byte array 
	if (len (data) < 1) :
		break
	mystring = data.decode()# A function as part of byte arrays that figures things out and decodes to unicode;
	print(mystring)
