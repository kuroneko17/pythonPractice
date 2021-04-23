#	python操作文件
---
###	读写文件
---
*	文件和文件路径
	-	文件有两个关键属性： “文件名” （通常写成一个单词）和“路径” 。路径指明了文件在计算机上的位置。
	-	根文件夹” ，它包含了所有其他文件夹。在 Windows 中，根文件夹名为 C:\，也称为 C：盘。在 OS X 和 Linux 中，根文件夹是/。在本书中，我使用 Windows 风格的根文件夹，C:\。如果你在 OS X 或 Linux 上输入交互式环境的例子，请用/代替。
	-	附加卷，诸如 DVD 驱动器或 USB 闪存驱动器，在不同的操作系统上显示也不同。在 Windows 上，它们表示为新的、带字符的根驱动器。诸如 D:\或 E:\。在 OS X上，它们表示为新的文件夹，在/Volumes 文件夹下。在 Linux 上，它们表示为新的文件夹，在/mnt（"mount"）文件夹下。同时也要注意，虽然文件夹名称和文件名在Windows 和 OS X 上是不区分大小写的，但在 Linux 上是区分大小写的。
	-	Windows 上的倒斜杠以及 OS X 和 Linux 上的正斜杠 
		*	os.path.join()  --  如果将单个文件和路径上的文件夹名称的字符串传递给它，os.path.join()就会返回一个文件路径的字符串， 包含正确的路径分隔符。
	-	当前工作目录
		*	os.getcwd()  --  取得当前工作路径的字符串
		*	os.chdir()  --  改变当前工作路径
			```
				# 如果要更改的当前路径不存在，则显示如下错误
				>>> os.chdir('C:window\\system32')
				Traceback (most recent call last):
				  File "<console>", line 1, in <module>
				FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'C:window\\system32'
				>>> os.chdir('C:windows\\system32')
			```
		*	os.makedirs() -- 创建新文件夹。
	-	绝对路径和相对路径
		*	有两种方法指定一个文件路径。
			-	“绝对路径”，总是从根文件夹开始
			-	“相对路径”，它相对于当前程序的当前工作目录。
			-	相对路径开始处的.\是可选的。例如，.\spam.txt 和 spam.txt 指的是同一个文件。 
			-	还有点（.）和点点（..）文件夹。它们不是真正的文件夹，而是可以在路径中使用的特殊名称。单个的句点（ “点” ）用作文件夹目名称时，是“这个目录”的缩写。两个句点（ “点点” ）意思是父文件夹。 
		*	处理绝对路径和相对路径
	-	os.path 模块
		*	os.path 模块包含了许多与文件名和文件路径相关的有用函数。[os.path官方参考文档](http://docs.python.org/3/library/os.path.html)
		*	os.path模块属性和方法
			-	os.path.sep  --  返回当前系统的分割符
			-	os.path.abspath(path) -- 将返回参数的绝对路径的字符串。这是相对路径转换为绝对路径的简便方法。
			-	os.path.isabs(path) -- 如果参数是一个绝对路径的话，返回True，如果是相对路径的话返回False。
			-	os.path.relpath(path, start)  --  将返回从start路径到path的相对路径的字符串，如果没有start参数，将从当前工作目录作为开始路径。
			-	os.path.dirname(path)  --  将返回一个字符串，它将包含path参数中最后一个斜杠之前的所有内容。(返回文件目录名)(返回上级目录)
			-	os.path.basename(path)  --  将返回一个字符串，它将包含path参数最后一个斜杠之后的所有内容。(返回文件名)
			-	os.path.split(path)  -- 返回一个包含路径的目录名称和基本名称的字符串元组。
			-	os.path.getsize(path)  --  返回path参数 中文件的字节数。
			-	os.listdir(path)  --  返回文件名字符串的列表，包含path 参数中的每个文件(只接受文件目录)
			-	os.path.exists(path)  --  如果path参数所指的文件或者文件目录存在的话，返回True，否则返回False。
			-	os.path.isfile(path)  --  如果path参数是一个文件的话，返回True，否则返回False。
			-	os.path.isdir(path)  -- 如果path参数是一个文件目录的话，返回True，否则返回False。
			-	os.path.getsize(file)  --  获取文件的大小
			```
				>>> os.makedirs("c:\\test\\one\\two\\three")
				>>> os.path.abspath('cwd')
				'C:\\windows\\system32\\cwd'
				>>> os.getcwd()
				'C:\\windows\\system32'
				>>> os.path.abspath('test')
				'C:\\windows\\system32\\test'
				>>> os.path.isabs('test')
				False
				>>> os.path.isabs('C:\\test\\one\\two')
				True
				>>> os.path.relpath('test1', 'C:')
				'test1'
				>>> os.path.relpath('test1',)
				'test1'
				>>> os.path.relpath('test1', '../')
				'system32\\test1'
				>>> os.path.relpath('test1', 'C:\\')
				'windows\\system32\\test1'
				>>> os.path.relpath('C:\\test\\one', 'C://MySelf')
				'..\\test\\one'
				>>> os.path.sep
				'\\'
				>>> path 
				Traceback (most recent call last):
				  File "<console>", line 1, in <module>
				NameError: name 'path' is not defined
				>>> path = 'C:test\\one\\two\\three\\testFile1.txt'
				>>> os.path.dirname(path)
				'C:test\\one\\two\\three'
				>>> os.path.basename(path)
				'testFile1.txt'
				>>> os.path.split(path)
				('C:test\\one\\two\\three', 'testFile1.txt')
				>>> (os.path.dirname(path), os.path.basename(path))
				('C:test\\one\\two\\three', 'testFile1.txt')
				>>> os.path.dirname(path).split(os.path.sep)
				['C:test', 'one', 'two', 'three']
				>>> path = "C:\\test\\one\\two\\three\\testFile1.txt"
				>>> os.path.getsize(path)
				39
				>>> os.listdir(os.path.dirname(path))
				['testFile1.txt']
				>>> os.listdir(os.path.dirname(path))
				['README.txt', 'testFile1.txt']
				>>> os.listdir(path)
				Traceback (most recent call last):
				  File "<console>", line 1, in <module>
				NotADirectoryError: [WinError 267] 目录名称无效。: 'C:\\test\\one\\two\\three\\testFile1.txt'
				>>> totalSize = 0
				>>> for file in os.listdir(os.path.dirname(path)):
						print('{} is {} bit'.format(file, os.getsize(os.path.dirname(path)+os.path.sep+file)))
				... ... 
				Traceback (most recent call last):
				  File "<console>", line 2, in <module>
				AttributeError: module 'os' has no attribute 'getsize'
				>>> for file in os.listdir(os.path.dirname(path)):
						print('{} is {} bit'.format(file, os.path.getsize(os.path.dirname(path)+os.path.sep+file)))
				... ... 
				README.txt is 29 bit
				testFile1.txt is 39 bit
				>>> os.path.isfile(path)
				True
				>>> os.path.isdir(path)
				False
				>>> os.path.exists(path)
				True
			```
*	文件的读写过程
	-	纯文本文件  --  只包含基本文本字符，不包含字体、大小和颜色信息。带有.txt 扩展名的文本文件，以及带有.py 扩展名的Python 脚本文件。你的程序可以轻易地读取纯文本文件的内容，将它们作为普通的字符串值。 
	-	二进制文件  --  是所有其他文件类型，诸如字处理文档、PDF、图像、电子表格和可执行程序。既然每种不同类型的二进制文件，都必须用它自己的方式来处理。许多模块让二进制文件的处理变得更容易。在本章稍后，你将探索其中一个模块：shelve。
	-	Python读写文件
		1.	打开文件，转换为python对象。调用open()函数，返回一个File对象。
		2.	对文件进行对或者写操作。调用file对象read()方法或者write()方法
		3.	关闭文件。调用File对象close()方法，关闭该文件。
	-	open函数
		*	 open()函数打开一个文件，就要向它传递一个字符串路径，表明希望打开的文件。这既可以是绝对路径，也可以是相对路径。open()函数返回一个 File 对象。这些命令都将以读取纯文本文件的模式打开文件，或简称为“读模式” 。当文件以读模式打开时， Python 只让你从文件中读取数据， 你不能以任何方式写入或修改它。在 Python 中打开文件时，读模式是默认的模式。但如果你不希望依赖于 Python 的默认值，也可以明确指明该模式，向 open()传入字符串'r'，作为第二个参数。
		*	 open()将返回一个 File 对象。File 对象代表计算机中的一个文件，它只是Python 中另一种类型的值， 就像你已熟悉的列表和字典。
		*	with open(fileName1, 'w+') as fn1, open('fileName2', 'r+') as fn2:(用with open() 方式打开文件不用主动调用close()关闭文件)
		*	open(fileName, 'type', encoding='utf-8', errors='ingore')参数 type=[r|r+|w|w+|a|a+|wb|rb]
*	读取文件内容
	-	文件读取
		*	fileObj.read()  --  返回fileObj的内容作为一整个大字符串
		*	fileObj.readlines()  --  把fileObj的内容作为一个按照换行符分隔开每一行作为一个字符串的字符串列表返回
*	写入文件内容
	-	Python 允许你将内容写入文件，方式与 print()函数将字符串“写”到屏幕上类似。但是，如果打开文件时用读模式，就不能写入文件。你需要以“写入纯文本模式”或“添加纯文本模式”打开该文件，或简称为“写模式”和“添加模式” 。
	-	写模式将覆写原有的文件，从头开始，就像你用一个新值覆写一个变量的值。将'w'作为第二个参数传递给 open()，以写模式打开该文件。不同的是，添加模式将在已有文件的末尾添加文本。你可以认为这类似向一个变量中的列表添加内容，而不是完全覆写该变量。将'a'作为第二个参数传递给 open()，以添加模式打开该文件。  
	-	如果传递给 open()的文件名不存在，写模式和添加模式都会创建一个新的空文件。在读取或写入文件后，调用 close()方法，然后才能再次打开该文件。 
	```
		>>> os.getcwd()
		'C:\\windows\\system32'
		>>> newPath = 'C:\\test\\one\\two\\now'
		>>> os.makedirs(newPath)
		>>> os.chdir(newPath)
		>>> os.getcwd()
		'C:\\test\\one\\two\\now'
		>>> baconFile = open(path+os.path.sep+'bacon.txt', 'w')
		Traceback (most recent call last):
		  File "<console>", line 1, in <module>
		FileNotFoundError: [Errno 2] No such file or directory: 'C:\\test\\one\\two\\three\\testFile1.txt\\bacon.txt'
		>>> baconFile = open(newPath+os.path.sep+'bacon.txt', 'w')
		>>> baconFile.write('# Hello World!!\n')
		16
		>>> baconFile.close()
		>>> baconFile.open(newPath+os.path.sep+'bacon.txt')
		Traceback (most recent call last):
		  File "<console>", line 1, in <module>
		AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
		>>> baconFile = open(newPath+os.path.sep+'bacon.txt')
		>>> baconFile.readlines()
		['# Hello World!!\n']
		>>> baconFile.close()
		>>> baconFile = open(newPath+os.path.sep+'bacon.txt', 'a')
		>>> baconFile.write('Bacon is not a vagetable.')
		25
		>>> baconFile.close()
		>>> baconFile = open(newPath+os.path.sep+'bacon.txt')
		>>> baconFile.read(newPath+os.path.sep+'bacon.txt')
		Traceback (most recent call last):
		  File "<console>", line 1, in <module>
		TypeError: argument should be integer or None, not 'str'
		>>> baconFile.read()
		'# Hello World!!\nBacon is not a vagetable.'
		>>> baconFile.close(0)
		Traceback (most recent call last):
		  File "<console>", line 1, in <module>
		TypeError: TextIOWrapper.close() takes no arguments (1 given)
		>>> baconFile.close()
		>>> testFile2 = open('testFile2.txt', 'w')
		>>> testFile2.write('This is test file2. \n')
		21
		>>> testFile2.close()
		>>> testFile2 = open('testFile2.txt', 'a')
		>>> testFile2.write('Append something new.')
		21
		>>> testFile2.close()
		>>> testFile2 = open('testFile2.txt')
		>>> testFile2.read()
		'This is test file2. \nAppend something new.'
	```
*	利用shelve模块保存变量(shelve模块)
	-	利用 shelve 模块，你可以将Python程序中的变量保存到二进制的shelf文件中。这样，程序就可以从硬盘中恢复变量的数据。shelve 模块让你在程序中添加“保存”和“打开”功能。例如，如果运行一个程序，并输入了一些配置设置，就可以将这些设置保存到一个 shelf 文件，然后让程序下一次运行时加载它们。
	-	shelveFile要先打开之后才能进行读写操作，不必用读模式或写模式打开，因为它们在打开后，既能读又能写。
	-	shelveFile也有keys()和values()方法，返回shelveFile的键和值类列表的值(对象)，需要先用list()转换为列表之后再使用。
*	将变量存储为模块(导入pprint模块利用pprint.printFormat()函数将变量保存为fileName.py文件)
	-	创建一个.py 文件（而不是利用 shelve 模块保存变量）的好处在于，因为它是一个文本文件，所以任何人都可以用一个简单的文本编辑器读取和修改该文件的内容。但是，对于大多数应用，利用 shelve 模块来保存数据，是将变量保存到文件的最佳方式。只有基本数据类型，诸如整型、浮点型、字符串、列表和字典，可以作为简单文本写入一个文件。例如，File 对象就不能够编码为文本。
	```
		>>> import sys,os
		>>> os.getcwd()
		'C:\\Users\\MakeNoSense'
		>>> os.chdir('C:\\test\\one\\two\\now')
		>>> os.getcwd()
		'C:\\test\\one\\two\\now'
		>>> os.listdir(os.getcwd())
		['bacon.txt', 'myCat.txt', 'myCats.py', 'mydata.bak', 'mydata.dat', 'mydata.dir', 'testFile2.txt', '__init__.py', '__pycache__']
		>>> import myCats as mc
		>>> mc.myCats
		[{'desc': 'chubby', 'name': 'zophis'}, {'desc': 'fluffy', 'name': 'pook'}]
	```
*	小练习
	-	examPaper(考卷问题)
	-	multiClipboard(剪贴板内容管理)
*	小结
	```
		文件被组织在文件夹中（也称为目录） ，路径描述了一个文件的位置。
		运行在计算机上的每个程序都有一个当前工作目录，它让你相对于当前的位置指定文件路径，
		而非总是需要完整路径（绝对路径） 。os.path 模块包含许多函数，用于操作文件路径。 
		你的程序也可以直接操作文本文件的内容。open()函数将打开这些文件，将它们的内容读取为一个大字符串
		（利用 reae()方法） ，或读取为字符串的列表（利用方法readlines()）。
		Open()函数可以将文件以写模式或添加模式打开，分别创建新的文本文件或在原有的文本文件中添加内容。 
		在前面几章中，你利用剪贴板在程序中获得大量文本，而不是通过手工输入。
		现在你可以用程序直接读取硬盘上的文件，这是一大进步。因为文件比剪贴板更不易变化。
		在下一章中，你将学习如何处理文件本身，包括复制、删除、重命名、移动等。 
	```

---

###	组织文件
---
*	shutil模块
	-	shutil（或称为 shell 工具）模块中包含一些函数，让你在 Python 程序中复制、移动、改名和删除文件。要使用 shutil 的函数，首先需要 import shutil。
	-	复制文件和文件夹
		*	shutil.copy(source, destination)  --  将source处的文件复制到路径destination处的文件夹，该函数返回一个字符串，表示被复制文件的路径(默认为当前文件路径下的destination文件夹，如果不存在则将destination作为新文件名保存在当前文件夹)
		*	shutil.copytree(folderName, targetFolder)  --  把指定文件夹复制到目标文件夹，返回目标文件夹字符串
	-	移动文件和文件夹
		*	shutil.move(source, destination)  -- 路径 source 处的文件夹移动到路径destination，并返回新位置的绝对路径的字符串。可用于重命名文件(如果目标文件夹中已经有同名文件则会被覆盖)
		*	shutil.
	-	删除文件和文件夹
		*	os.unlink(path)  --  删除path处的文件
		*	os.rmdir(path)  --  删除path处的文件夹，文件夹必须为空
		*	shutil.rmtree()  --  删除 path 处的文件夹， 它包含的所有文件和文件夹都会被删除。
		```
		# 删除文件时应注意，先打印出要删除的文件再确认删除
		import os, shutil
		for filename in os.listdir():
			if filename.endswith('.txt'):
				# os.unlink(filename)
				print(filename)
		``` 
		*	安全删除文件
			-	导入第三方模块，send2trash	
			-	send2trash.send2trash(filename)  --  把指定文件发送到计算机回收站
	-	遍历目录树
		*	os.walk()函数被传入一个字符串值，即一个文件夹的路径。
		```
		os.walk()函数被传入一个字符串值，即一个文件夹的路径。你可以在一个 for
		循环语句中使用 os.walk()函数，遍历目录树，就像使用 range()函数遍历一个范围的
		数字一样。不像 range()，os.walk()在循环的每次迭代中，返回 3 个值： 
		1．当前文件夹名称的字符串。 
		2．当前文件夹中子文件夹的字符串的列表。 
		3．当前文件夹中文件的字符串的列表。 
		所谓当前文件夹，是指 for 循环当前迭代的文件夹。程序的当前工作目录，不
		会因为 os.walk()而改变。 
		就像你可以在代码 for i in range(10):中选择变量名称 i 一样， 你也可以选择前面
		列出来的 3 个字的变量名称。我通常使用 foldername、subfolders 和 filenames。 
		```
	-	用zipfile压缩文件
		*	导入zipfile模块，使用zipfile.ZipFile(zipFileName)返回一个ZipFile对象(类似python打开一个文件返回一个对象)
		*	读取.zip文件
			-	zipfileName.namelist(), gitinfo(), file_size, compress_size
			```
			import zipfile
			zipFileName = 'zipFileTest.zip'
			zipfileName = zipfile.ZipFile(zipFileName)
			zipfileName.namelist()
			txtFile = zipfileName.getinfo('testFolder/b.txt')
			txtFile.file_size #  文件大小
			txtFile.compress_size # 文件压缩后大小
			# 计算文件压缩率
			round(txtFile.compress_seze / txtFile.file_size, 2)
			zipfileName.close()
			```
		*	从zip文件中解压
			-	zipfileName.extractall(extractFolder)  解压压缩包到指定文件夹
		 	-	zipfileName.extract(fileInZip, extractFolder)  解压压缩包文件到指定文件夹
		 	```
		 	>>> newZipFile = zipfile.ZipFile('testFolder.zip')
			>>> newZipFile.extract('testFolder/b.txt', '..')
			'..\\testFolder\\b.txt'
			>>> newZipFile.close()
			>>> newZipFile = zipfile.ZipFile('../testFolder.zip')
			>>> newZipFile.extractall('..')
			>>> newZipFile.close()
			ZipFile 对象的 extractall()方法从 ZIP 文件中解压缩所有文件和文件夹，放到当
			前工作目录中。你可以向extractall()传递的一个文件夹名称， 它将文件解压缩到那个文件夹， 
			而不是当前工作目录。如果传递给 extractall()方法的文件夹不存在，它会被创建。
			传递给 extract()的字符串，必须匹配 namelist()返回的字符串列表中的一个。或
			者，你可以向 extract()传递第二个参数，将文件解压缩到指定的文件夹，而不是当
			前工作目录。如果第二个参数指定的文件夹不存在，Python 就会创建它。extract()
			的返回值是被压缩后文件的绝对路径。 
		 	```
		*	创建和添加到zip文件
			-	要创建你自己的压缩 ZIP 文件，必须以“写模式”打开 ZipFile 对象，即传入'w'作为第二个参数（这类似于向 open()函数传入'w'，以写模式打开一个文本文件） 。
			-	newZipFile = zipfile.ZipFile('newZipFileName.zip', 'w/a')
				newZipFile.write('fileName/FolderName', compress_type=zipfile.ZIP_DEFLATED)
				newZipFile.close()
			```
			>>> newZipFile = zipfile.ZipFile('testZipFolder.zip', 'w')
			>>> newZipFile.write('testFolder', compress_type=zipfile.ZIP_DEFLATED)
			>>> newZipFile.close()
			这段代码将创建一个新的 ZIP 文件， 名为new.zip， 它包含spam.txt 压缩后的内容。  
			要记住，就像写入文件一样，写模式将擦除 ZIP 文件中所有原有的内容。如果
			只是希望将文件添加到原有的 ZIP 文件中，就要向 zipfile.ZipFile()传入'a'作为第二
			个参数，以添加模式打开 ZIP 文件。 
			```
	-	小实验
		*	项目：将带有美国风格日期的文件改名为欧洲风格日期(renameDates.py)
		*	项目：将一个文件夹备份到一个 ZIP 文件 (backUpToZip.py)