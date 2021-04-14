# zeroDivede.py

import random

def spam(devideBy):
	# try :
	return 43 / devideBy
	# except ZeroDivisionError:
	# 	print('Error:Invalid argument.')

try :
	for i in range(0,12):
		randomNum = random.randint(0,1)
		print(spam(randomNum))
except ZeroDivisionError:
	print('Error:Invalid argument.')

# while True:
# 	ramdomNum = random.randint(0,123)
# 	print(spam(randomNum))

# # zeroDivede.py

# import random

# def spam(devideBy):
# 	return 42 / devideBy

# while True:
# 	randomNum = random.randint(0,123)
# 	print(spam(randomNum))

# try :
# 	return 52 / devideBy
# except ZeroDivisionError:
# 	print('Invalid argument')