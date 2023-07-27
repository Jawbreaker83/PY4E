#  In object oriented programming, a constructor in a class is a speacial block of statements
#  called when an object is created.

class PartyAnimal:
	x = 0 

	def __init__(self):#This constructor and the destructor below are optiion and they are typically used to set up variables.
		print('I am constructed')

	def party(self):
		self.x = self.x + 1
		print('So Far', self.x)

	def __del__(self):
		print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)







