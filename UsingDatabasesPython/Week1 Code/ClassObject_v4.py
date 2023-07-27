#Two independent instances;

class PartyAnimal:
	x = 0 
	name = "" #Internal variable
	def __init__(self, z):
		self.name = z
		print(self.name,'constructed')

	def party(self):
		self.x = self.x + 1
		print('self.name', 'party count', self.x)

s = PartyAnimal('Sally')
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()

#  In this updated code, the PartyAnimal class has been extended to include an __init__ constructor method and an additional internal variable name. 
#  Let's go through the code step by step:

#  1. We define the PartyAnimal class with two class variables: x and name.
#  2. We define an __init__ method within the class, which is a constructor method. This method is called when an instance of the class is created. 
#     The __init__ method takes two parameters: self (as usual) and z. It sets the name instance variable to the value of the z parameter and prints a 
#     message indicating that the object has been constructed.
#  3. The party() method remains unchanged from the previous code. It increments the x counter by 1 and prints the current count of parties attended (self.x).

#  The output indicates the following steps:
#  1.  We create an instance s of the PartyAnimal class and pass 'Sally' as the argument for the z parameter. The constructor sets the name instance variable 
#      to 'Sally', and we get the message 'Sally constructed'.
#  2.  We call the party() method on the s instance. It increments the x counter to 1 and prints 'self.name' (which is 'Sally') and the current count of
#      parties attended (1).
#  3.  We create another instance j of the PartyAnimal class and pass 'Jim' as the argument for the z parameter. The constructor sets the name instance 
#      variable to 'Jim', and we get the message 'Jim constructed'.
#  4.  We call the party() method on the j instance. It increments the x counter to 1 and prints 'self.name' (which is 'Jim') and the current count of 
#      parties attended (1).
#  5.  We call the party() method on the s instance again. Since s and j are different instances, they have separate x counters. So, this call 
#      increments s's x counter to 2 and prints 'self.name' (which is 'Sally') and the current count of parties attended (2).
#  6.  Each instance of the class has its own separate set of instance variables, and changes made to one instance do not affect the others.





