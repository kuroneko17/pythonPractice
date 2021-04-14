# regexResult.py

"""
	编写一个程序，打开文件夹中所有的.txt 文件，查找匹配用户提供的正则表达式的所有行。
	结果应该打印到屏幕上。 
"""

import sys, os, re

# 定义查找内容函数
# @regex -> 正则表达式，fileName -> 文件名
def getContent(regex, fileName):
	# 读取文件内容
	txtFile = open(fileName)
	txtContent = txtFile.read()
	txtFile.close()
	# 根据正则表达式查找内容
	regexObj = re.compile(regex)
	regexResult = regexObj.findall(txtContent)
	# 返回结果
	return regexResult

# 获取当前文件夹所有文件的文件名，如果为空文件夹则打印提示
fileNameList = os.listdir(os.getcwd())
if not fileNameList:
	print('This folder is null.')
	sys.exit()
# 遍历文件名列表，构造txt文件的文件名列表
txtFileList = []
for fileName in fileNameList:
	if os.path.isfile(fileName) and fileName[-4:] == '.txt':
		txtFileList.append(fileName)
# 如果该文件夹没有txt文件则打印提示
if not txtFileList:
	print('There is no .txt file in this folder.')
	sys.exit()
# 获取用户输入的正则表达式
print('Type your regex:')
regexStr = input()

# 使用getContent函数获取内容并打印结果
for txtFileName in txtFileList:
	txtFile = getContent(regexStr, txtFileName)
	print('The results of {}:'.format(txtFileName))
	print(txtFile)
	print('='*50)
