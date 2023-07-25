#Tuples are 'immutable'; unlike a list once you create a tuple you cannot alter its contents - similiar to a string
#LISTS ARE MUTABLE AND STRINGS AND TUPLES ARE NOT!


#A Lists are mutable, here we change a 7 to a 6
x = [9,8,7]
x[2] = 6
print(x)

#A 3 character string and we would like to change the c to a d
#y = 'ABC'
#y[2] = 'D'

#A Tuple, it is not immutable cannot change the 3 to a 0
z = (5,4,3)
z[2] = 0