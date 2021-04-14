# picnicTable.py

"""
	---PICNIC ITEMS-- 
	sandwiches.. 4 
	apples...... 12 
	cups........ 4 
	cookies..... 8000 
	-------PICNIC ITEMS------- 
	sandwiches.......... 4 
	apples.............. 12 
	cups................ 4 
	cookies............. 8000
"""
def printPicnic(picnicItem, leftWidth, rightWidth):
	print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
	for k, v in picnicItem.items():
		print(k.ljust(leftWidth, '-') + str(v).rjust(rightWidth, '-'))

picnicItems = {'sandwichs': 5, 'apples': 12, 'cups': 4, 'cookies': 50}
printPicnic(picnicItems, 12, 7)
printPicnic(picnicItems, 17, 9)
