#The given Python code uses regular expressions to extract the URL from the given line containing an HTML anchor tag (<a>). Let's go through
#the code step-by-step:

#import re: Import the Python re module, which provides support for regular expressions.

#line = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>': Define a string variable line that contains an HTML snippet with an anchor tag (<a>).

#url_pattern = r'<a\s+href="([^"]+)">': Define the regular expression pattern url_pattern to match the anchor tag with its href attribute. 
#The pattern uses r to indicate a raw string, which is helpful for dealing with backslashes in regular expressions. The expression captures everything 
#inside the double quotes after href= using the ([^"]+) capturing group.

#match = re.search(url_pattern, line): Use the re.search() function to find the first occurrence of the regular expression pattern in the line string. 
#If the pattern is found, match will be a match object; otherwise, it will be None.

#if match:: Check if the re.search() function found a match.

#url = match.group(1): If there was a match, use the group(1) method of the match object to extract the contents of the capturing group 
#(URL inside the double quotes) from the match.

#print(url): Print the extracted URL.

#else:: If no match was found, print "No URL found."

#When you run this code with the given line, it will extract and print the URL "http://www.dr-chuck.com" from the line since it matches the specified pattern. 
#The output will be:

import re

line = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'

# Using regular expression to extract the URL
url_pattern = r'<a\s+href="([^"]+)">'
match = re.search(url_pattern, line)

if match:
    url = match.group(1)
    print(url)
else:
    print("No URL found.")

