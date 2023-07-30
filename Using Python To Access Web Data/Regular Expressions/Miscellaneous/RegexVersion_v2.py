 #But we can do a similar thing with regular expressions and we've seen this with dual split. So, this is the find way of pulling that out, dual split is, we split it into words with spaces, then we grab the second one, we split that by at signs and then we grab the second piece of that. So, we take the second word, we split that second word by at sign, and then we take the second piece, and then we get this. So, we were able to do that with four lines, a little more elegant. But if we do regular expressions, we can say, hey, go find me an at sign, followed by some number of non-blank characters. I don't want to extract the at sign, see where I put the parentheses, I want to start extracting after the at sign and up to the rest of those non-blank characters. So, that says "buf," I've got what I want. So, it's a way to say in a little expression.



import re

lin = ('From Stephen.Marquard@uct.ac.za Sat Jan 5 09:14:16 2008')
y = re.findall('^From .*@([^ ]*)', lin)
print(y)

