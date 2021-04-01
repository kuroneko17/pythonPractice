# User.py
class User():
	
	def __init__(self, firstName, lastName, age, sex, profession, **item):
		self.firstName = firstName.title()
		self.lastName = lastName.title()
		self.name = self.firstName + ' ' + self.lastName
		self.age = age
		self.sex = sex
		self.profession = profession
		self.loginAttempts = 0

	def describeUser(self):
		print('{} is a {} and {} years old.'.format(self.name, self.profession, self.age))
	def greetUser(self):
		print('Hello ' + self.name + '.')
	def setLoginAttempts(self, time):
		self.loginAttempts = time
	def getLoginAttempts(self):
		return self.loginAttempts
	def incrementLoginAttempts(self):
		self.loginAttempts += 1
	def resetLoginAttempts(self):
		self.loginAttempts = 0

"""
lisaWhite = User('lisa','white', 23, 0, 'reporter')
lisaWhite.describeUser()
lisaWhite.greetUser()

hutmLee = User('hutm', 'lee', 21, 1, 'acter')
print(hutmLee.getLoginAttempts())
hutmLee.incrementLoginAttempts()
print(hutmLee.getLoginAttempts())
hutmLee.incrementLoginAttempts()
hutmLee.incrementLoginAttempts()
hutmLee.incrementLoginAttempts()
print(hutmLee.getLoginAttempts())
hutmLee.resetLoginAttempts()
print(hutmLee.getLoginAttempts())
"""

class Privileges():

	def __init__(self, addPrivilege=None):
		self.privileges = ['can add post', 'can delete post', 'can add user', 'can ban user']
		if addPrivilege:
			self.privileges.append(addPrivilege)
	def showPrivileges(self):
		print('Admin has following privileges:')
		for privilege in self.privileges:
			print(privilege)

class Admin(User):

	def __init__(self, firstName, lastName, age, sex, profession, privileges=None):
		super().__init__(firstName, lastName, age, sex, profession)
		self.privileges = Privileges(addPrivilege='recover user post')
	# def showPrivileges(self):
	# 	print('Admin has following privileges:')
	# 	for privilege in self.privileges:
	# 		print(privilege)

# tuileChen = Admin('tuile', 'Chen', 24, 1, 'no-job', ['can add post', 'can delete post', 'can add user', ' can ban user'])
# tuileChen.describeUser()
# tuileChen.showPrivileges()
yashNoe = Admin('yash', 'Noe', 23, 1, 'None')
yashNoe.privileges.showPrivileges()