#If you want a special regular expression character to just behave normally you prefix it with '\'.

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)