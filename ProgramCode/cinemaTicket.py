# cinemaTicket.py

# 导入正则表达式模块
import re

while True:
	# 打印提示信息，获取用户输入年龄
	print('How old are you?Type "quit" to quit.')
	age = input()
	# 对用户输入进行校验
	numRegex = re.compile(r'^\d+$')
	# 当正则表达时匹配为空时
	if numRegex.search(age) == None:
		# 当用户输入时'quit'时，退出循环
		if age == 'quit':
			break
		# 当用户输入为其他时，返回提示信息
		print('You should enter number or "quit" ')
	# 当用户输入时数字时
	else:
		age = int(age)
		if age < 3:
			print('You are free.')
		elif 3 <= age <= 12:
			print('You should pay $10 for the ticket.')
		elif age > 12:
			print('You should pay $15 for the ticket.')
 

# prompt = "how old are you "
# prompt += "enter 'quit' when you  are finished.\n"

# while True:
# 	age = input(prompt)
# 	if age == 'quit':
# 		break
# 	else:
# 		# 对用户输入进行判断，用异常捕捉来进行判断
# 		try:
# 			age = int(age)
# 		except ValueError:
# 			print('Error! You should enter number or "quit" ')
# 			break
# 		if age < 3:
# 			print('you are free')
# 		elif age < 12:
# 			print('you should pay $10 for the ticket')
# 		else:
# 			print('you should pay $15 for the ticker')