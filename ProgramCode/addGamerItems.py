# addGamerItems.py

def addToInventory(inventory, addedItems):
	# reward = {}
	# for i in addedItems:
	# 	reward.setdefault(i, 0)
	# 	if i in reward.keys():
	# 		reward[i] += 1
	# print(reward)
	for i in addedItems:
		if i in inventory.keys():
			inventory[i] += 1
		else:
			inventory.setdefault(i, 0)
			inventory[i] += 1
	print(inventory)
	sum = 0
	# print('Inventory:')
	for k, v in inventory.items():
		print('-   {}  {}'.format(v, k))
		sum += v
	print('Total number of items: {}'.format(sum))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)