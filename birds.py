import random
class Bird:
	def __init__(self, name, age, airspeed):
		self.name = name
		self.age = age
		self.airpseed = airspeed 
		self.alive = True

class Parrot(Bird):
	lifespan = 60

	def __init__(self, fn, age, name):
		self.fn = fn
		self.alive = True
		airspeed = 10
		super().__init__(name, age, airspeed)
		

	def squawk(self):
		self.fn()

	def birthday(self):
		self.age += 1
		death = random.random() * self.age / self.lifespan
		if death > 0.8:
			print("You're dead")
			self.alive = False
			return	
	
#while p.age < 60:
#	p.birthday()
#	if p.alive
#	print(p.age)

