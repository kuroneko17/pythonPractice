#! python3
# isPhoneNumber.py
"""
	假设你希望在字符串中查找电话号码。你知道模式：3 个数字，一个短横线，3个数字，
	一个短横线，再是 4 个数字。例如：415-555-4242。 
	假定我们用一个名为 isPhoneNumber()的函数， 来检查字符串是否匹配模式， 它返回 True 或 False。
"""

#	非正则表达式查找
def isPhoneNumber(text):
	if len(text) != 12:
		return False
	else:
		numList = text.split('-')
		if len(numList) != 3:
			return False
		else:
			for i in range(0, len(numList)):
				if not numList[i].isdecimal():
					return False
				else:
					if i < (len(numList) -1):
						if len(numList[i]) != 3:
							return False
					else:
						if len(numList[i]) != 4:
							return False	
			return True

# print('Enter the phone number:')
# phoneNumber = input()
# if phoneNumber:
# 	print(isPhoneNumber(phoneNumber))
# else:
# 	print('Please enter your phone number!')

"""
def isPhoneNumber(text): 
	if len(text) != 12: 
		return False 
	for i in range(0, 3): 
		if not text[i].isdecimal(): 
			return False 
	if text[3] != '-': 
		return False 
	for i in range(4, 7): 
		if not text[i].isdecimal(): 
			return False 
	if text[7] != '-': 
		return False 
	for i in range(8, 12): 
		if not text[i].isdecimal(): 
			return False 
	return True 
"""

# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
	chuck = message[i:i + 12]
	if isPhoneNumber(chuck):
		print('Phone number was found : {}'.format(chuck))
print('Done')

"""
for i in range(len(message)): 
	chunk = message[i:i+12] 
	if isPhoneNumber(chunk): 
		print('Phone number found: ' + chunk) 
print('Done')
"""