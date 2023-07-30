#The comparison operators work with tuples and other sequences.  If the first item
#is equal, python goes on to the next element, and so on until it 
#finds elements that differ;

x=(0,1,2) < (5,1,2)
print(x)
y = (0,1,2000000) < (0,3, 4)
print(y)
z = ('Jones','Sally') < ('Jones','Sam')
print(z)
a  = ('Jones', 'Sally') > ('Adams' , 'Sam')
print(a)
