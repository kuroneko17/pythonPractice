# randomExamPaper.py

"""
	假如你是一位地理老师，班上有 35 名学生，你希望进行美国各州首府的一个小测验。
	不妙的是，班里有几个坏蛋，你无法确信学生不会作弊。
	你希望随机调整问题的次序，这样每份试卷都是独一无二的，这让任何人都不能从其他人那里抄袭答案。
	当然，手工完成这件事又费时又无聊。好在，你懂一些 Python。 
	下面是程序所做的事： 
	•  创建 35 份不同的测验试卷。 
	•  为每份试卷创建 50 个多重选择题，次序随机。 
	•  为每个问题提供一个正确答案和 3 个随机的错误答案，次序随机。 
	•  将测验试卷写到 35 个文本文件中。 
	•  将答案写到 35 个文本文件中。 
	这意味着代码需要做下面的事： 
	•  将州和它们的首府保存在一个字典中。 
	•  针对测验文本文件和答案文本文件，调用 open()、write()和 close()。 
	•  利用 random.shuffle()随机调整问题和多重选项的次序。

	optionRandNum = random.randint(len(cap.captitals)+1)
	Where is the capital of {}?
	A) 
	B) 
	C) 
	D) 
"""
import sys, os, random, capitals as cap

# 记录所有的州，打乱顺序
stateList = []
for key in cap.capitals.keys():
	stateList.append(key)

for paperNum in range(1, 36):
	# 记录考卷问题和答案
	question = ''
	answer = ''

	random.shuffle(stateList)
	# 循环所有的州
	for i in range(1, len(stateList)+1):
		# 每次循环记录省会列表，作为选项
		capitalList = []
		for value in cap.capitals.values():
			capitalList.append(value)
		# 打印问题
		# print('{}. Where is the capital of {}?'.format(i, stateList[i-1]))
		# 拼接每一个问题
		question += '{}. Where is the capital of {}?\n'.format(i, stateList[i-1])

		# 选项字母
		optionLetters = ['A', 'B', 'C', 'D']
		# 为每个问题新建选项列表
		optionList = []
		# 把答案写进选项列表中，再从省会列表中去除，避免生成重复选项
		optionList.append(cap.capitals[stateList[i-1]])
		capitalList.remove(cap.capitals[stateList[i-1]])
		#	生成随机的省会，补充作为选项列表
		for j in range(3):
			optionList.append(capitalList.pop(random.randint(0, len(capitalList)-1)))
			j -= 1
		# 打乱选项列表
		random.shuffle(optionList)
		# 根据选项字母遍历，打印所有选项
		for n in range(0, len(optionLetters)):
			# print('{}. {}'.format(optionLetters[n], optionList[n]))
			question += '{}. {}\n'.format(optionLetters[n], optionList[n])
			# 记录答案
			if optionList[n] == cap.capitals[stateList[i-1]]:
				# 拼接每一个问题的答案
				answer += '{}. {}\n'.format(i, optionLetters[n])
		# print(answer)

	# 判断存放试题的目录是否存在， 没有则新建
	if not os.path.exists('paper'):
		os.makedirs('paper')
	# 判断存放答案的目录是否存在，没有则新建
	if not os.path.exists('answer'):
		os.makedirs('answer')

	# 记录每份试题
	paperFile = open('paper{}paper{}.txt'.format(os.path.sep, paperNum), 'w')
	paperFile.write(question)
	paperFile.close()

	# 记录每份试题的答案
	answerFile = open('answer{}answer{}.txt'.format(os.path.sep, paperNum), 'w')
	answerFile.write(answer)
	answerFile.close()

	# print(question)
	# print(answer)
"""
test = 0
while True:
	randnum = random.randint(0, 10)
	print(randnum)
	if randnum == 10:
		print(randnum)
		print('randnum is 10')
		break
	elif test == 20:
		print(str(test)+'test is 20.Break out the code.')
		break
	test += 1
sys.exit()
"""
# for key, value in cap.capitals.items():
# 	print('Where is the capital of {}?'.format(key))
# 	print('A) {}'.format(capitalList[random.randint(0, len(capitalList)-1)]))
# 	print('B) {}'.format(capitalList[random.randint(0, len(capitalList)-1)]))
# 	print('C) {}'.format(cap.capitals[key]))
# 	print('D) {}'.format(capitalList[random.randint(0, len(capitalList)-1)]))
# 	print('='*50)
# 	# print('The capital of {} is {}.'.format(key, value))
