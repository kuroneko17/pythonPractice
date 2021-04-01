# Restaurant.py
# 创建Restaurant类
class Restaurant():
	#	初始化方法
	def __init__(self, restaurantName, cuisineType):
		self.name = restaurantName
		self.cuisineType = cuisineType
		self.numberServed = 0
	# 打印餐厅描述
	def describeRestaurant(self):
		print('There is a restaurant named {}.And it style is {}'.format(self.name, self.cuisineType))
	# 打印餐厅正在营业中
	def openRestaurant(self):
		print('Restaurant {} is opening.'.format(self.name))
	# 设置初始用餐人数
	def setNumberServed(self, number):
		self.numberServed = number
	def getNumberServed(self):
		return self.numberServed
	# 增加用餐人数
	def incrementNumberServed(self, number):
		if number >= 0:
			self.numberServed += number
		else:
			return 'Number must be positive.'
"""
restaurant = Restaurant('restaurant', 'ChineseFood')
print(restaurant.name)
print(restaurant.cuisineType)
restaurant.describeRestaurant()
restaurant.openRestaurant()

restaurant.setNumberServed(23)
print(restaurant.getNumberServed())
restaurant.incrementNumberServed(12)
print(restaurant.getNumberServed())
"""
class IcecreamStand(Restaurant):

	def __init__(self, restaurantName, cuisineType, flavors):
		super().__init__(restaurantName, cuisineType)
		self.flavors = flavors
	def getAllFlavor(self):
		allFlavor = []
		for flavor in self.flavors:
			flavorIcecream = flavor + ' ice-cream'
			allFlavor.append(flavorIcecream)
		return allFlavor
	def showAllIcecream(self):
		allFlavorIcecream = self.getAllFlavor()
		print('All Ice-cream:')
		for icecream in allFlavorIcecream:
			print(icecream)

iceCreamStand = IcecreamStand('ice-cream stand', 'ice-cream', ['apple', 'banana', 'mochi'])
iceCreamStand.showAllIcecream()