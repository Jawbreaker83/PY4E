#Since HTTP is som common, we have a library that does all the socket work for us
#and makes web pages look like a file;

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
	print(line.decode().strip())#line.decode convert the byte array to a string
	