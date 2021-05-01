# mapIt.py

"""
Web 浏览器的选项卡将打开 URL http://inventwithpython.com/。这大概就是
webbrowser模块能做的唯一的事情。既使如此，open()函数确实让一些有趣的事情成为可
能。例如，将一条街道的地址拷贝到剪贴板，并在Google 地图上打开它的地图，这是很
繁琐的事。你可以让这个任务减少几步，写一个简单的脚本，利用剪贴板中的内容在浏
览器中自动加载地图。这样，你只要将地址拷贝到剪贴板，运行该脚本，地图就会加载。  
你的程序需要做到： 
•  从命令行参数或剪贴板中取得街道地址。 
•  打开 Web 浏览器，指向该地址的 Google 地图页面。 
这意味着代码需要做下列事情： 
•  从 sys.argv 读取命令行参数。 
•  读取剪贴板内容。 
•  调用 webbrowser.open()函数打开外部浏览器。 
打开一个新的文件编辑器窗口，将它保存为 mapIt.py。
"""
import sys, pyperclip, webbrowser, requests, bs4

# https://map.gaode.com/search?query=
def mapIt(url):
	keyword = ''
	# 判断是否是命令行参数是否存在，在的话就作为关键字，没有就从将剪贴板内容作为关键字
	if len(sys.argv) < 2:
		keyword = pyperclip.paste()
	else:
		keyword = sys.argv[1]

	url = url + '/search?query=' + keyword
	
	# print(url)
	# sys.exit()

	webbrowser.open(url)

"""
回顾一下，下载并保存到文件的完整过程如下： 
1．调用 requests.get()下载该文件。 
2．用'wb'调用 open()，以写二进制的方式打开一个新文件。 
3．利用 Respose 对象的 iter_content()方法做循环。 
4．在每次迭代中调用 write()，将内容写入该文件。 
5．调用 close()关闭该文件。
"""
# 下载文件保存到硬盘
def getWebPage(url):
	# 请求网页
	res = requests.get(url)
	# print(res.status_code)
	# print(len(res.text))
	# print(len(res.text[:500]))
	#	try: ... except: ... 检查错误，查看文件是否下载成功
	try:
		res.raise_for_status()
	except Exception as exc:
		print('There is a Exception: {}'.format(exc))
	# 用二进制方式写入文件
	file = open('testWebPage.html', 'wb')
	for chunk in res.iter_content(100000):
		# print(chunk)
		file.write(chunk)
	file.close()


url = 'http://www.gaode.com'
# url = 'http://www.twitch.com'
# url = 'http://localhost/test1.jpg'
# mapIt(url)
getWebPage(url)