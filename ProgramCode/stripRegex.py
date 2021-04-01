# stripRegex.py

"""
	# strip()的正则表达式版本 
	写一个函数，它接受一个字符串，做的事情和 strip()字符串方法一样。
	如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。
	否则，函数第二个参数指定的字符将从该字符串中去除。 
"""

import re, pyperclip

def stripRegex(text, delString = None ):
	resultText = ''
	if delString:
		textRegex = re.compile(delString)
		resultText = textRegex.sub('', text)
	else:
		# textRegex = re.compile(r'(\s+)([\S]+)(\s+)')
		# textRegex = re.compile(r'(\s+)(.+?)(\s+)')
		textRegex = re.compile(r'(^\s*)|(\s*$)')
		# textRegex = re.compile(r'^[\S]+')
		print(textRegex.search(text).groups())
		resultText = textRegex.sub('', text)
	return resultText

print('Enter your string:')
text = input()
print('Please enter the string that you want to delete: (blank for doing nothing)')
delString = input()
print(stripRegex(text, delString))