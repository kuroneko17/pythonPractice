# backUpToZip.py

"""
假定你正在做一个项目，它的文件保存在C:\AlsPythonBook 文件夹中。你担心工作
会丢失，所以希望为整个文件夹创建一个ZIP 文件，作为“快照” 。你希望保存不同的版
本，希望 ZIP 文件的文件名每次创建时都有所变化。例如 AlsPythonBook_1.zip、
AlsPythonBook_2.zip、AlsPythonBook_3.zip，等等。你可以手工完成，但这有点烦人，
而且可能不小心弄错ZIP 文件的编号。 运行一个程序来完成这个烦人的任务会简单得多。  
针对这个项目，打开一个新的文件编辑器窗口，将它保存为 backupToZip.py。
"""

import sys, os, zipfile
# 打包成.zip文件备份
def backUpToZip(path):
	# path = os.path.abspath(path)
	# 第一次备份，zip文件编号为1，如果已经存在了，编号就累加
	bNum = 1
	while True:
		zipName = path + '_' + str(bNum) + '.zip'
		if not os.path.exists(zipName):
			break
		elif not os.path.isfile(zipName):
			break
		bNum += 1
		
	zipFile = zipfile.ZipFile(zipName, 'w')
	print('Creating ' + zipName)
	for folder, subFolders, fileNames in os.walk(path):
		zipFile.write(folder, compress_type=zipfile.ZIP_DEFLATED)
		print('Adding file in ' + folder)
		# for subFolder in subFolders:
		# 	zipFile.write(subFolder, compress_type=zipfile.ZIP_DEFLATED)
		for fileName in fileNames:
			zipFile.write(folder + os.path.sep + fileName, compress_type=zipfile.ZIP_DEFLATED)

	zipFile.close()
	print('DONE!')

# path = 'spam'
path = 'C:\\test'
backUpToZip(path)