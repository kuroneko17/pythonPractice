# gamerItems.py

gameItmes = {
							'rope': 1, 'torch': 6, 'gold coin': 42, 'degger': 1, 'arrow': 12
						}

def displayInventory(items):
	print('Inventory:')
	sum = 0
	for k, v in items.items():
		print('-  {} {}'.format(v, k))
		sum += v
	print('Total num of items: {}'.format(sum))

displayInventory(gameItmes)
