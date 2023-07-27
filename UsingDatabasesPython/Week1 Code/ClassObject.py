class PartyAnimal:
	x = 0 

	def party(self):
		self.x = self.x + 1
		print('So Far', self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

print('Type', type(an))
print('Dir', dir(an))

# This code defines a class called PartyAnimal with a class variable x and a method party(). The x variable keeps track of the number of parties attended,
# and the party() method increments the counter and prints the current count of parties attended.

# Let's go through the code step by step:

# We define the PartyAnimal class with a class variable x initialized to 0.  We define a method within the class named party(), which takes in self
# as its first parameter. In Python, self is a reference to the instance of the object, and it is always the first parameter of instance methods.
# Inside the party() method, we increment the x counter by 1 and print the current count of parties attended (self.x).
# After defining the class, we create an instance of PartyAnimal called an. Then, we call the party() method on the an instance three times consecutively. 
# Each time the method is called, the counter x is incremented, and the current count of parties attended is printed.

# The output indicates that the party() method was called three times on the an instance, and the counter x was incremented accordingly. 
# The first call sets x to 1, the second call sets x to 2, and the third call sets x to 3.




