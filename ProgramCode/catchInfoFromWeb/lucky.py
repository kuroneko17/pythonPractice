# lucky.py

"""
每次我在 Google 上搜索一个主题时，都不会一次只看一个搜索结果。通过鼠
标中键点击搜索结果链接，或在点击时按住 CTRL 键，我会在一些新的选项卡中打
开前几个链接，稍后再来查看。我经常搜索 Google，所以这个工作流程 （开浏览器，
查找一个主题，依次用中键点击几个链接）变得很乏味。如果我只要在命令行中输
入查找主题，就能让计算机自动打开浏览器，并在新的选项卡中显示前面几项查询
结果，那就太好了。让我们写一个脚本来完成这件事。 
下面是程序要做的事： 
•  从命令行参数中获取查询关键字。 
•  取得查询结果页面。 
•  为每个结果打开一个浏览器选项卡。 
这意味着代码需要完成以下工作： 
•  从 sys.argv 中读取命令行参数。 
•  用 requests 模块取得查询结果页面。 
•  找到每个查询结果的链接。 
•  调用 webbrowser.open()函数打开 Web 浏览器。 
打开一个新的文件编辑器窗口，并保存为 lucky.py。 
"""

import sys, webbrowser, requests, bs4
# 获取关键词使用搜素引擎打开网页
def openPageOnBrowser():
	
	# 使用google引擎搜索
	# gurl = 'https://google.com/search'
	# 使用bing引擎搜索
	burl = 'https://cn.bing.com/search'
	# 构造requests.get()传递参数
	urlParam = {}
	# 如果是以命令行打开，则第二个参数为搜索关键词，否则让用户输入关键词
	if len(sys.argv) > 2:
		urlParam['q'] = sys.argv[1]
	else:
		print('Enter the keyword that you want to search:')
		urlParam['q'] = input()
	# 获取搜索结果
	res = requests.get(burl, params = urlParam)
	# 判断requests.get()是否正常
	try:
		res.raise_for_status()
	except Exception as exc:
		print('Error: ' + str(exc))
	# 把获取的文本以html格式打开
	resSoup = bs4.BeautifulSoup(res.text, 'html.parser')
	# google搜索结果的a元素
	# resAElem = resSoup.select('.yuRUbf a')
	# bing搜索结果的a元素
	resAElem = resSoup.select('.b_algo a')
	# 要打开的网页的最小数
	nums = min(5, len(resAElem))
	for i in range(nums):
		# a元素的跳转链接
		# testurl = resAElem[i].get('href')
		webbrowser.open(resAElem[i].get('href'))

openPageOnBrowser()