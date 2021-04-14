# Car.py
class Car():

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		# 为让这个类更有趣，下面给它添加一个随时间变化的属性，它存储汽车的总里程。
		self.odometerReading = 0
		self.gasTank = 40

	def getDescriptiveName(self):
		longName = str(self.year) + ' ' + self.make + ' ' + self.model
		return longName

	def readOdometer(self):
		print('This car has ' + str(self.odometerReading) + ' miles on it.')
		# return self.odometerReading
	# 如果有替你更新属性的方法，将大有裨益。这样，你就无需直接访问属性，
	# 而可将值传递给一个方法，由它在内部进行更新。
	#	可对方法update_odometer()进行扩展， 使其在修改里程表读数时做些额外的工作。 
	#	下面来添加一些逻辑，禁止任何人将里程表读数往回调：
	def updateOdometer(self, mileage):
		if mileage >= self.odometerReading:
			self.odometerReading = mileage
		else:
			return 'Error!You can\'t roll back an odometer.'
		# 你可以轻松地修改这个方法，以禁止增量为负值，从而防止有人利用它来回拨里程表。
	def incrementOdometer(self, miles):
		if miles >= 0:
			self.odometerReading += miles
		else:
			return 'Error!Miles must more than 0.'
	def fillGasTank(self):
		return self.gasTank

# myCar = Car('audi', 'A4', 2014)
# print(myCar.getDescriptiveName())
# myCar.odometerReading = 123
# myCar.readOdometer()
# myCar.updateOdometer(345)
# myCar.readOdometer()
# myCar.incrementOdometer(90)
# myCar.readOdometer()

# Battery类
class Battery():

	def __init__(self, batterySize=70):
		self.batterySize = batterySize
	def describeBattery(self):
		return 'This car has a ' + str(self.batterySize) + '-kWh battery.'
	def getRange(self):
		if self.batterySize == 70:
			rangeMiles = 240
		elif self.batterySize == 85:
			rangeMiles = 270
		elif self.batterySize == 120:
			rangeMiles = 360
		message = 'This car can go aproximately ' + str(rangeMiles) + ' miles on a full charge.'
		return message
	def upgradeBattery(self):
		if self.batterySize < 85:
			self.batterySize = 85
"""
	对于ElectricCar类的特殊化程度没有任何限制。模拟电动汽车时，你可以根据所需的准确程度添加任意数量的属性和方法。
	如果一个属性或方法是任何汽车都有的，而不是电动汽车特有的，就应将其加入到Car类而不是ElectricCar类中。
	这样，使用Car类的人将获得相应的功能，而ElectricCar类只包含处理电动汽车特有属性和行为的代码。 
"""
# ElectricCar()类继承自父类Car()
class ElectricCar(Car):
	# 子类的初始化方法
	def __init__(self, make, model, year):
		# 初始化父类的属性
		super().__init__(make, model, year)
		# self.battery = 70
		self.battery = Battery()
	"""
		例如，不断给ElectricCar类添加细节时，我们可能会发现其中包含很多专门针对汽车电瓶的属性和方法。
		在这种情况下，我们可将这些属性和方法提取出来，放到另一个名为Battery的类中，
		并将一个Battery实例用作ElectricCar类的一个属性：
	"""
	# def describeBattery(self):
	# 	# return 'This car has a ' + str(self.battery) + '-kWh battery.'
	# 	return self.battery.describeBattery()
	def fillGasTank(self):
		return 'ElectricCar has no gas tank.'

# myTesla = ElectricCar('tesla', 'model s', 2016)
# print(myTesla.getDescriptiveName())
# print(myTesla.battery.describeBattery())
# print(myTesla.battery.getRange())

testTesla = ElectricCar('tesla', 'Model S', 2018)
print(testTesla.getDescriptiveName())
print(testTesla.battery.getRange())
testTesla.battery.upgradeBattery()
print(testTesla.battery.getRange())
