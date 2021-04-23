# renameDates.py

"""
	假定你的老板用电子邮件发给你上千个文件，文件名包含美国风格的日期
	（MM-DD-YYYY） ，需要将它们改名为欧洲风格的日期（DD-MM-YYYY） 。手 工 完
	成这个无聊的任务可能需要几天时间！让我们写一个程序来完成它。 
	下面是程序要做的事： 
	•  检查当前工作目录的所有文件名，寻找美国风格的日期。 
	•  如果找到，将该文件改名，交换月份和日期的位置，使之成为欧洲风格。 
	这意味着代码需要做下面的事情： 
	•  创建一个正则表达式，可以识别美国风格日期的文本模式。 
	•  调用 os.listdir()，找出工作目录中的所有文件。 
	•  循环遍历每个文件名，利用该正则表达式检查它是否包含日期。 
	•  如果它包含日期，用 shutil.move()对该文件改名。 
	对于这个项目，打开一个新的文件编辑器窗口，将代码保存为 renameDates.py。  
"""

import sys, os, re, shutil
# 重命名文件
def renameDate(folder):
	# 把指定文件夹中的所有文件名取出来
	allFiles = []
	for file in os.listdir(folder):
		fileName = '{}{}{}'.format(folder, os.path.sep, file)
		if os.path.isfile(fileName):
			allFiles.append(fileName)

	# na风格日期表达式
	naFormatRegex = re.compile(r"""
		^(.*?)						# 匹配日期以外的文件前缀
		(0?\d|1[12])				# 匹配月份
		[-|\r+|_|.|\\|/]		# 分隔符
		(0?\d|[1-3]\d)			# 匹配日期
		[-|\r+|_|.|\\|/]		# 分隔符
		((19|20|21)\d{2})		# 匹配年份
		(.*?)$						# 匹配日期以外的文件后缀
		""", re.VERBOSE)

	for fileName in allFiles:
		# 匹配符合条件的文件名
		newNameList = naFormatRegex.findall(fileName)
		if newNameList:
			# 把匹配到结果，重组为文件新名称
			beforepart = newNameList[0][0]
			month = newNameList[0][1]
			day = newNameList[0][2]
			year = newNameList[0][3]
			afterpart = newNameList[0][5]
			newName = '{}{}-{}-{}{}'.format(beforepart, day, month, year, afterpart)
			# 重命名文件
			shutil.move(fileName, newName)

path = 'spam'
renameDate(path)
# 匹配日期的正则表达式
# 应为存在大小月份，和特殊情况(闰年)，所以使用分组匹配处理
# 匹配年份 ((19|20|21)\d{2})
# 匹配大月(1,3,5,7,8,10,12)  (0?[13578] | 1[02])
# 匹配小月(4,6,9,11)  (0?[469]|11)
# 处理2月份,