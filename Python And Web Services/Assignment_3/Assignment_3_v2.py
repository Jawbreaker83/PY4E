#sample_url = "http://python-data.dr-chuck.net/comments_42.html"


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

#Grab the html information and parse it with BeautifulSoup
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#To obtain a list with the "span" tags
tags = soup('span')

#To count the sum of all the values within the span tags
count = 0
for tag in tags:

#Inserted to cast the result as integers apart from the text string.
	count += int(tag.contents[0])
print(count)#Getting a list with the "span" tags