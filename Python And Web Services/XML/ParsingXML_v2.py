

import xml.etree.ElementTree as ET
input ='''<stuff>
	<users>
		<user x='2'>
			<id>001</id>
			<name>Chuck</name>
		</user>
		<user x = '7'>
			<id>009</id>
			<name>Brent</name>
		</user>
	</users>
</stuff>'''

#Python code that will go through each of the XML tags above
stuff = ET.fromstring(input)#All of the text from above is passed into the fromstring and we get an object returned called stuff
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
	print('Name', item.find('name').text)
	print('id', item.find('id').text)
	print('Attribute', item.get('x'))