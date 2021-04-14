# Die.py
from random import randint

class Die():

	def __init__(self, sides=6):
		self.sides = sides

	def rollDie(self):
		return randint(1,self.sides)

sixSidesDie = Die()
for i in range(10):
	print(sixSidesDie.rollDie())

print('='*20)
tenSidesDie = Die(10)
for i in range(10):
	print(tenSidesDie.rollDie())

print('='*20)
twentySidesDie = Die(20)
for i in range(10):
	print(twentySidesDie.rollDie()) 