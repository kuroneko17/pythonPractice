# makeDateFileTest.py
# 创建日期测试文件，生成随机日期名称文件
import sys, os, random
# 创建文件夹
def mkdir(path):
	# 判断文件夹是否存在
	if not os.path.exists(path):
		os.makedirs(path)
	elif not os.path.isdir(path):
		os.makedirs(path)

	return path
# 创建随机日期名文件
# @path -> 指定文件夹, @fileContent -> 文件内容, @fileName -> 文件名
def mkfile(path, fileContent, fileName=''):
	# monthList = list(range(1, 13))
	# dayList = list(range(1,32))
	month = random.randint(1, 12)
	day = random.randint(1, 31)
	if month < 10:
		month = '0' + str(month)
	if day < 10:
		day = '0' + str(day)
	# 年份
	years = [19, 20, 21]
	year = random.randint(0, 99)
	if year < 10:
		year = '0' + str(year)
	year = '{}{}'.format(random.choice(years), year)
	# 拼接文件名
	fileName = '{}{}{}-{}-{}-{}.txt'.format(path, os.path.sep, fileName,  month, day, year)
	# 新建文件，写入文件
	newFile = open(fileName, 'w', encoding='utf-8')
	newFile.write(content)
	newFile.close()

path = mkdir('spam')
content = 'test.\nHello world.'
for i in range(13):
	mkfile(path, content, fileName='spam')