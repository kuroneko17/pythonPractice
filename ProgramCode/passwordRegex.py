# passwordRegex.py

"""
	# 强口令检测 
	写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。
	强口令的定义是：长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字。
	你可能需要用多个正则表达式来测试该字符串，以保证它的强度。 
"""

import sys, re, pyperclip
def passwordCheck(password):
	passwordRegex = re.compile(r'.{8,}')
	passwordUpperRegex = re.compile(r'[A-Z]+')
	passwordLowerRegex = re.compile(r'[a-z]+')
	passwordNumRegex = re.compile(r'\d+')

	if passwordRegex.search(password) == None:
		return False
	if passwordUpperRegex.search(password) == None:
		return False
	if passwordLowerRegex.search(password) == None:
		return False
	if passwordNumRegex.search(password) == None:
		return False
	return True

while True:
	print('Please enter your password:')
	password = input()
	if passwordCheck(password):
		print('Your password is strong enough.')
		break
	else:
		print('Your password is not safily,please enter again')