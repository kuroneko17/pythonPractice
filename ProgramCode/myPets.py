# myPets.py

myPets = ['shiro', 'inu', 'kuro', 'neko']
pet = input('Please enter your pets: ')

if pet in myPets:
	print('{} is your pet.'.format(pet))
else:
	print('I dont have a pet named {}'.format(pet))