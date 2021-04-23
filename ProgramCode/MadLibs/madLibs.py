# madLibs.py

"""
	创建一个疯狂填词（Mad Libs）程序，它将读入文本文件，
	并让用户在该文本文件中出现 ADJECTIVE、 NOUN、 ADVERB 或 VERB 等单词的地方，加上他们自己的文本。
	例如，一个文本文件可能看起来像这样：

	The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events. 

	程序将找到这些出现的单词，并提示用户取代它们。 
	Enter an adjective: 
	silly 
	Enter a noun: 
	chandelier 
	Enter a verb: 
	screamed 
	Enter a noun: 
	pickup truck 
	以下的文本文件将被创建：
	The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events. 

	 结果应该打印到屏幕上，并保存为一个新的文本文件。 
"""

import sys, os

# 定义文件名和替代词组
fileName = 'madLibs.txt'
replaceWord = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

# 判断文件是否存在，没有则新建
if not os.path.exists(fileName):
	content = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events. '
	madLibsFile = open(fileName, 'w')
	madLibsFile.write(content)
	madLibsFile.close()

# 读取文件，打印文件内容
madLibsFile = open(fileName)
madLibsText = madLibsFile.read()
madLibsFile.close()
print(madLibsText)

# 把文件内容转换为列表处理
madLibsTextList = madLibsText.strip().split(' ')
# 遍历文本内容
for i in range(len(madLibsTextList)):
	# 处理包含句点的词
	dotMark = False
	# if madLibsTextList[i].endswith('.')
	if madLibsTextList[i][-1] == '.':
		dotMark = True
		madLibsTextList[i] = madLibsTextList[i][:-1]
	"""
	dot = ''
	if madLibsTextList[i].endswith('.'):
		dot += madLibsTextList[i][-1]
	
	... ...

	if dot:
		madLibsTextList[i] += dot
	"""

	# 遍历替代词组，判断文本内容列表中是否存在需要替换的词，有就获取用户输入替代
	for rword in replaceWord:
		if rword == madLibsTextList[i] :
			print('Enter one word is {}.Or enter to shut down,but your typing will not save.'.format(rword.lower()))
			newWord = input()
			if newWord:
				madLibsTextList[i] = newWord
			else:
				sys.exit()
	# 补回句点
	if dotMark:
		madLibsTextList[i]  += '.'
# 替换后的文本内容列表转换为字符串
madLibsText = ' '.join(madLibsTextList)

# 新建文件保存替换后的文本内容
newFileName = 'new' + fileName.title()
madLibsFile = open(newFileName, 'w')
madLibsFile.write(madLibsText)
madLibsFile.close()
# 读取文本内容并打印
madLibsFile = open(newFileName)
print(madLibsFile.read())
madLibsFile.close()