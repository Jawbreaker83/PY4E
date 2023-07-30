import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

sample_data = 'http://py4e-data.dr-chuck.net/comments_42.xml'
actual_data = 'http://py4e-data.dr-chuck.net/comments_1831418.xml'

data_url = actual_data
data = urllib.request.urlopen(data_url).read()

xml_data = ET.fromstring(data)
search_str = 'comments/comment'
count_tags = xml_data.findall(search_str)

total_count = 0
for tag in count_tags:
	count = tag.find('count')
	total_count += int(count.text)

print(total_count)