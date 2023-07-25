#Extracting data from JSON

import urllib.request, urllib.parse, urllib.error
import json

sample_json_data = 'http://py4e-data.dr-chuck.net/comments_42.json'
actual_json_data = 'http://py4e-data.dr-chuck.net/comments_1831419.json'

urldata = urllib.request.urlopen(actual_json_data).read()
data = json.loads(urldata)

total = 0
for comment in data['comments']:
	total += comment['count']

print('TOTAL SUM: ', total)




