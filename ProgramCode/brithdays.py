# brithdays.py

brithdays = {'Alice': 'Dec. 12th', 'Bob': 'Jar. 1st', 'Cathlin': 'Ferb. 23th','Doge': 'Mar. 7th'}

while True:
	print('Enter a name: (blank to exit)')
	name = input()
	if not name:
		break
	else :
		if name in brithdays:
			print('{}\'s brithday is {}.'.format(name,brithdays[name]))
		else:
			brithday = ''
			while not brithday:
				print('what is {}\'s brithday:'.format(name))
				brithday = input()
				if not brithday:
					print('Please enter the brithday of {}'.format(name))
			brithdays[name] = brithday
		print('Brithday database updated.')
		print('Now your note of your firends\' brithday:')
		for i in brithdays:
			print('{}\'s brithday is {}.'.format(i,brithdays[i]))

