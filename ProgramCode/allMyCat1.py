# allMyCat1.py

# myCatName1 = input('Please enter your cats\' name: ')
# myCatName2 = input('Please enter your cats\' name: ')
# myCatName3 = input('Please enter your cats\' name: ')
# myCatName4 = input('Please enter your cats\' name: ')
# myCatName5 = input('Please enter your cats\' name: ')

# print('Your cats\' names are {}, {}, {}, {}, {}'.format(myCatName1, myCatName2, myCatName3, myCatName4, myCatName5))

catName = []
while True:
	name = input('Enter the name of your cat' + str(len(catName) + 1) + ' (Or enter nothing to stop.):')
	if name == '':
		break
	catName += [name]

print('The cat names are: ')
for name in catName:
	print(name)