

import xml.etree.ElementTree as ET
data = '''<person>
	<name>Chuck</name>
	<phone type = "intl">
		+1 734 303 4456
	</phone>
	<email hide ='yes'/>
</person>'''

tree = ET.fromstring(data)#Fromstring says take this string data and give us back a nice tree construct;
print('Name:', tree.find('name').text)#if you want the text between the tags use this;
print('Attr:',tree.find('email').get('hide')) # if you want the attribute use this call the get method.