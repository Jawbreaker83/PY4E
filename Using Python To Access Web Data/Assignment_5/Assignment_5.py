#In this assignment you will write a Python program and the program will prompt for a URL, read the XML data from that URL using urllib and then parse 
#and extract the comment counts from the XML data, compute the sum of the numbers in the file.  We provide two files for this assignment. One is a sample 
#file where we give you the sum for your testing and the other is the actual data you need to #process for the assignment.

#The data consists of a number of names and comment counts in XML as follows:


#You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that shows how to parse XML is geoxml.py.
#But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import xml.etree.ElementTree as ET

sample_data = "http://py4e-data.dr-chuck.net/comments_42.xml"
actual_data = "http://py4e-data.dr-chuck.net/comments_1831418.xml"

#We'll analyze this generic parameter, so we will only need to change its source and not every single one of its appearances in the code #NOTE: I'm using Sublime
#Text and it doesn't accept raw_input, so I'll set the URL #from here isntead from a user prompt
data_url = actual_data
data = urllib.request.urlopen(data_url).read()

#xml_data contains the commentinfo object, as it is the main structure, so we have to look for the comments element and then for all its comment elements;
xml_data = ET.fromstring(data)
search_str = "comments/comment"
count_tags = xml_data.findall(search_str)

#Computing the sum
total_count = 0
for tag in count_tags:
	#We'll find the "count" element inside each "comment" element and add it 
	count = tag.find('count')
	total_count += int(count.text)

print(total_count)
