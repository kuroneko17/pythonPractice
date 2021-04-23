# treeFolder.py

import os

path = 'C:\\test'
for folderName, subFolderNames, fileNames in os.walk(path):
	print('Current folder is {}.'.format(folderName))
	for subFolder in subFolderNames:
		print('SUBFOLDER OF {}:  {}'.format(folderName, subFolder))
	for file in fileNames:
		print('THE FILE INSIDE {} IS {}'.format(folderName, file))

print('')