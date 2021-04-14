#! python3
# phoneAndEmail.py
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
"""
	假设你有一个无聊的任务，要在一篇长的网页或文章中，找出所有电话号码和邮件地址。
	如果手动翻页，可能需要查找很长时间。如果有一个程序，可以在剪贴板的文本中查找电话号码和 E-mail 地址，
	那你就只要按一下 Ctrl-A 选择所有文本，按下 Ctrl-C 将它复制到剪贴板， 然后运行你的程序。 
	它会用找到的电话号码和 E-mail地址，替换掉剪贴板中的文本。
"""

"""
	你的电话号码和 E-mail 地址提取程序需要完成以下任务：
	  从剪贴板取得文本。 
	  找出文本中所有的电话号码和 E-mail 地址。 
	  将它们粘贴到剪贴板。 
	现在你可以开始思考，如何用代码来完成工作。代码需要做下面的事情： 
	  使用 pyperclip 模块复制和粘贴字符串。 
	  创建两个正则表达式，一个匹配电话号码，另一个匹配 E-mail 地址。 
	  对两个正则表达式，找到所有的匹配，而不只是第一次匹配。 
	  将匹配的字符串整理好格式，放在一个字符串中，用于粘贴。 
	  如果文本中没有找到匹配，显示某种消息。 
"""

"""
	1. 先构造电话号码和电子邮箱的正则表达式
	2.	从粘贴板上的文本匹配所有对应的文本
	3.	从返回的结果构造成文本传回粘贴板

	#  **先对匹配到的结果进行处理(匹配到返回的结果是元组)**，之后在处理成文本粘贴到粘贴板上
"""
import sys, pyperclip, re

# 构造正则表达式
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?						# area code 区号
	(\s|-|\.)?										# separator 分隔符
	(\d{3})											# first 3 digits 开始3位数字
	(\s|-|\.)										# separator 分隔符
	(\d{4})											# last 4 digits 最后4位数字
	(\s*(ext|x|ext.)\s*(\d{2,5}))?		# extension 描述
	)''', re.VERBOSE)
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+		# username
	@									# symbol
	[a-zA-Z0-9.-]+				# domain name
	(\.[a-zA-Z]{2,4})			# dot-something
	)''', re.VERBOSE)

# 粘贴板匹配对应文本
text = str(pyperclip.paste())
phoneMatches = phoneRegex.findall(text)
emailMatches = emailRegex.findall(text)
# print(phoneMatches)
# print(emailMatches)

# 构造匹配结果
matches = []
# 构造文本返回给粘贴板
result = 'PhoneNumber: \n'
#	处理匹配结果，用'-'拼接电话号码。
#	再转换为字符串传递给粘贴板
if phoneMatches:
	matches.append('Phone Number:\n')
	for groups in phoneMatches:
		# if i == (len(phoneMatches) - 1):
		phoneNum = '-'.join([groups[1], groups[3], groups[5]])
		if groups[8] != '':
			phoneNum += ' x ' + groups[8]
		matches.append(phoneNum)
else :
	matches.append('Phone Number was not found.\n')

if emailMatches:
	matches.append('\n Email Address: \n')
	for groups in emailMatches:
		matches.append(groups[0])
else:
	matches.append('Email Address was not found.\n')
# pyperclip.copy(result)
# print(matches)
pyperclip.copy(' \n'.join(matches))

"""
	类似程序的构想 
	识别文本的模式（并且可能用 sub()方法替换它们）有许多不同潜在的应用。 
	  寻找网站的 URL，它们以 http://或 https://开始。 
	  整理不同日期格式的日期（诸如 3/14/2015、03-14-2015 和 2015/3/14） ，用唯一的标准格式替代。 
	  删除敏感的信息，诸如社会保险号或信用卡号。 
	  寻找常见打字错误，诸如单词间的多个空格、不小心重复的单词，或者句子末
	尾处多个感叹号。它们很烦人！ ！
"""

"""
	如何写一个正则表达式，匹配每 3 位就有一个逗号的数字？它必须匹配以下数字：
	  '42' 
	  '1,234' 
	  '6,368,745' 
	但不会匹配： 
	  '12,34,567' （逗号之间只有两位数字） 
	  '1234' （缺少逗号）
"""
#	?
numRegex = re.compile(r'(\d{3}\,)')
"""
	如何写一个正则表达式，匹配姓 Nakamoto 的完整姓名？
	你可以假定名字总是出现在姓前面，是一个大写字母开头的单词。该正则表达式必须匹配：
	  'Satoshi Nakamoto' 
	  'Alice Nakamoto' 
	  'RoboCop Nakamoto' 
	但不匹配： 
	  'satoshi Nakamoto'（名字没有大写首字母） 
	  'Mr. Nakamoto'（前面的单词包含非字母字符） 
	  'Nakamoto' （没有名字） 
	  'Satoshi nakamoto'（姓没有首字母大写） 
"""
nameRegex = re.compile(r'[A-Z][a-zA-Z]+\s+[A-Z][a-zA-Z]+')
"""
	如何编写一个正则表达式匹配一个句子，它的第一个词是 Alice、Bob 或
	Carol，第二个词是 eats、pets 或 throws，第三个词是 apples、cats 或 baseballs。
	该句子以句点结束。这个正则表达式应该不区分大小写。它必须匹配： 
	  'Alice eats apples.' 
	  'Bob pets cats.' 
	  'Carol throws baseballs.' 
	  'Alice throws Apples.' 
	  'BOB EATS CATS.' 
	但不匹配： 
	  'RoboCop eats apples.' 
	  'ALICE THROWS FOOTBALLS.' 
	  'Carol eats 7 cats.' 
"""
sentenseRegex = re.compile(r'''(
	(Alice|Bob|Carol)
	\s
	(eats|pets|throws)
	\s
	(apples|cats|baseballs)
	\.
	)''', re.IGNORECASE | re.VERBOSE)
"""
	# 强口令检测 
	写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。
	强口令的定义是：长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字。
	你可能需要用多个正则表达式来测试该字符串，以保证它的强度。 
"""
pwRegex = re.compile(r'')
"""
	# strip()的正则表达式版本 
	写一个函数，它接受一个字符串，做的事情和 strip()字符串方法一样。
	如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。
	否则，函数第二个参数指定的字符将从该字符串中去除。 
"""