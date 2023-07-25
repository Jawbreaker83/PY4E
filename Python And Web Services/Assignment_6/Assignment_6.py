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




#import urllib
#import json

#sample_url = "http://python-data.dr-chuck.net/comments_42.json"
#data_url = "http://python-data.dr-chuck.net/comments_277465.json"

#Reading the URL and parsing its data
#urldata = urllib.urlopen(data_url).read()
#data = json.loads(urldata)

#Finding each "count" field and adding its value to the total sum.
#total = 0
#for comment in data["comments"]:
#	total += comment["count"]

#print("TOTAL SUM: ", total)