# countFoods.py

allGuests = {
						'Alice': {'apples': 5, 'pretzels': 12}, 
						'Bob': {'ham sandwiches': 3, 'apples': 2}, 
						'Carol': {'cups': 3, 'apple pies': 1}
					}

def totalBrought(allItem):
	numBrought = 0
	items = {}
	# print(type(allItem))
	# exit()
	for k, v in allItem.items():
		for key, value in v.items():
			items.setdefault(key, 0)
			items[key] = items[key] + value
			# print(items)
		# print('{} brought {} {}')
	print('List of all items: ')
	for k, v in items.items():
		print('-   {}   {}'.format(k, v))

totalBrought(allGuests)