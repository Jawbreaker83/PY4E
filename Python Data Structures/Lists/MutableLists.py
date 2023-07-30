#Strings are 'immutable' we cannot change the contents of a string, we must make a new string to make 
#any change; List are 'Mutable', we can change an element of a list using the index 
#operator

fruit = 'banana'
#fruit[0] = 'b'

x = fruit.lower()
print(x)

lotto = [2,14,26,41,64]
print(lotto)

lotto[2] = 28
print(lotto)

