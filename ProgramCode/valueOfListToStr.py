# valueOfListToStr.py

def returnToStr(ListParameter):
	resultStr = ''
	for i in  range(0, len(ListParameter)):
		if i == 0:
			resultStr = str(ListParameter[i])
		elif i == (len(ListParameter) - 1):
			resultStr = resultStr + ' and ' + str(ListParameter[i])
		else:
			resultStr = resultStr + ', ' + str(ListParameter[i])
	return resultStr

try :
	# spam = input('Enter a lists: ')
	# print(type(spam))
	# exit()
	spam = ['apples', 'bananas', 'tofu', 'cats']
	# spam = [1, 32, 5, 523, 'apples', 'bananas', 'tofu', 'cats']
	print(returnToStr(spam))
except ValueError:
	print('ValueError.Pelase enter a list.')