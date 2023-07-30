
class PartyAnimal:
	x = 0 
	name = "" #Internal variable
	def __init__(self, nam):
		self.name = nam 
		print(self.name,'constructed')

	def party(self):
		self.x = self.x + 1
		print('self.name', 'party count', self.x)

class FootballFan(PartyAnimal):
	points = 0
	def touchdown(self):
		self.points = self.points + 7
		self.party()
		print(self.name, 'points', self.points)

s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()

#  In this updated code, a new class FootballFan has been created, which inherits from the PartyAnimal class. The FootballFan class adds an additional 
#  method touchdown() and a new class variable points.

#  Let's go through the code step by step:

#  1.  We define the PartyAnimal class as before, with a class variable x, an internal variable name, and an __init__ constructor method to initialize 
#      the name instance variable.

#  2.  We define a party() method in the PartyAnimal class, which increments the x counter by 1 and prints the current count of parties attended (self.x) 
#      and the name of the party animal (self.name).

#  3.  We define a new class called FootballFan, which inherits from the PartyAnimal class (it's specified in the parentheses after the class name). 
#      This means that FootballFan will have all the attributes and methods of PartyAnimal, as well as its own unique attributes and methods.

#  4.  Within the FootballFan class, we define a new class variable points to keep track of the number of points scored by the football fan.

#  5.  We define a new method within the FootballFan class called touchdown(). This method increments the points counter by 7 (assuming each touchdown 
#      scores 7 points) and then calls the party() method (inherited from PartyAnimal) to increment the x counter and print the current count of parties 
#      attended. After that, it prints the name of the football fan (self.name) and the current number of points (self.points).

#  6.  In this updated code, a new class FootballFan has been created, which inherits from the PartyAnimal class. The FootballFan class adds an additional 
#       method touchdown() and a new class variable points.

#  Let's go through the code step by step:

#  1.  We define the PartyAnimal class as before, with a class variable x, an internal variable name, and an __init__ constructor method to initialize 
#      the name instance variable.

#  2.  We define a party() method in the PartyAnimal class, which increments the x counter by 1 and prints the current count of parties attended (self.x) 
#      and the name of the party animal (self.name).

#  3.  We define a new class called FootballFan, which inherits from the PartyAnimal class (it's specified in the parentheses after the class name). 
#      This means that FootballFan will have all the attributes and methods of PartyAnimal, as well as its own unique attributes and methods.

#  4.  Within the FootballFan class, we define a new class variable points to keep track of the number of points scored by the football fan.

#  5.  We define a new method within the FootballFan class called touchdown(). This method increments the points counter by 7 
#      (assuming each touchdown scores 7 points) and then calls the party() method (inherited from PartyAnimal) to increment the x counter and 
#      print the current count of parties attended. After that, it prints the name of the football fan (self.name) and the current number of points (self.points).



