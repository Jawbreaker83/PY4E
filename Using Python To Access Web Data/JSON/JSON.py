#JSON represents data as nested 'lists' and 'dictionaries'

import json
data = '''{
	"name": "Chuck",
	"phone": {
		"type": "intl",
		"number": "+1 734 303 4456"
	},
	"email": {
		"hide": "yes"
	}
}'''

info = json.loads(data)#This is essentially a python dictionary created from this process; Loads the JSON stuff and does all of the parsing and creates an object called info
print('Name:', info['name'])
print('Hide:', info['email']['hide'])