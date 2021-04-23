# copyFile.py

"""
	选择性拷贝 
	编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg） 。
	不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中。 
"""
import os, shutil, re

# 复制指定格式得文件
def copyFile(path, targetPath):
	# 获取绝对路径
	path = os.path.abspath(path)
	targetPath = os.path.abspath(targetPath)
	# 判断目录路径存不存在
	if not os.path.exists(targetPath):
		os.makedirs(targetPath)
	elif os.path.isfile(targetPath):
		os.makedirs(targetPath)
	# 遍历目录中符合田间得文件
	for folder, subFolders, files in os.walk(path):
		# print('FolderName is : '+ folder)
		# for subFolder in subFolders:
		# 	print('SubFolder is : '+ subFolder)
		for file in files:
			if file.endswith('.pdf') or file.endswith('.jpg'):
				print('Copy file is : '+ file + ' in ' + folder + ' to {}.'.format(targetPath))
				shutil.copy(folder + os.path.sep + file, targetPath)

	print('Done!')

"""
	删除不需要的文件 
	一些不需要的、巨大的文件或文件夹占据了硬盘的空间，这并不少见。如果你
	试图释放计算机上的空间，那么删除不想要的巨大文件效果最好。但首先你必须找
	到它们。 
	编写一个程序，遍历一个目录树，查找特别大的文件或文件夹，比方说，超过
	100MB的文件 （回忆一下， 要获得文件的大小， 可以使用 os 模块的 os.path.getsize()） 。
	将这些文件的绝对路径打印到屏幕上。
"""
# 查找文件
def findFile(path):
	# 获取绝对路径
	path = os.path.abspath(path)
	# 查找文件大于100MB的
	for folder, subFolders, files in os.walk(path):
		for file in files:
			fileName = '{}{}{}'.format(folder, os.path.sep, file)
			if os.path.getsize(fileName) > 100*1024*1024:
				print('The file: \n {} \n is {:.2f}MB bigger than 100MB.'.format(fileName, os.path.getsize(fileName)/(1024*1024)))
	print('Done!')

"""
	消除缺失的编号 
	编写一个程序， 在一个文件夹中， 找到所有带指定前缀的文件， 诸如 spam001.txt, 
	spam002.txt 等，并定位缺失的编号（例如存在 spam001.txt 和 spam003.txt，但不存
	在 spam002.txt） 。让该程序对所有后面的文件改名，消除缺失的编号。 
	作为附加的挑战， 编写另一个程序，在一些连续编号的文件中， 空出一些编号，
	以便加入新的文件。
"""
# 
def checkFileNum(path):
	path = os.path.abspath()
	files = []
	spamRegex = re.compile(r'(spam)(\d){3}(.txt)$')

	for file in os.listdir(files):
		if os.path.isfile(file) and spamRegex.search(file):
			files.append(file)

	# TODO: check out the number of file sort.
	# for file in files:
	# 	fileName = '{}{}{}'.format(path, os.path.sep, file)
	# 	newFileName = '{}{}{}'.format(path, os.path.sep, file)
	# 	shutil.move(fileName, newFileName)


# path = 'C:\\test'
# path = 'F:\\2FTPFiles'
path = 'experiment/spam'
targetPath = '../folder'

# copyFile(path, targetPath)
findFile(targetPath)