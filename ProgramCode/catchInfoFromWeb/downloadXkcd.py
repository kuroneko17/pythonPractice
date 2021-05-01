# downloadXkcd.py

"""
博客和其他经常更新的网站通常有一个首页， 其中有最新的帖子， 以及一个 “前
一篇”按钮，将你带到以前的帖子。然后那个帖子也有一个“前一篇”按钮，以此
类推。这创建了一条线索，从最近的页面，直到该网站的第一个帖子。如果你希望
拷贝该网站的内容，在离线的时候阅读，可以手工导航至每个页面并保存。但这是
很无聊的工作，所以让我们写一个程序来做这件事。 
XKCD 是一个流行的极客漫画网站，它符合这个结构（参见图 11-6） 。首页
http://xkcd.com/有一个“Prev”按钮，让用户导航到前面的漫画。手工下载每张漫
画要花较长的时间，但你可以写一个脚本，在几分钟内完成这件事。 
下面是程序要做的事： 
•  加载主页； 
•  保存该页的漫画图片； 
•  转入前一张漫画的链接； 
•  重复直到第一张漫画。
这意味着代码需要做下列事情： 
•  利用 requests 模块下载页面。 
•  利用 Beautiful Soup 找到页面中漫画图像的 URL。 
•  利用 iter_content()下载漫画图像，并保存到硬盘。 
•  找到前一张漫画的链接 URL，然后重复。 
打开一个新的文件编辑器窗口，将它保存为 downloadXkcd.py。 
"""

# 站点url： http://xkcd.com/  

import sys, requests, bs4, os

# 下载图片  prevUrl -> 上一页的url后缀
def downloadPicture(prevUrl=''):

	# 判断存储图片的文件夹是否存在，没有则新建
	# os.makedirs(picFolder, exist_ok=True) 
	picFolder = 'xkcdPicture'
	if not os.path.exists(picFolder):
		os.makedirs(picFolder)
	if not os.path.isdir(picFolder):
		os.makedirs(picFolder)

	# 初始的url为主页
	turl = 'http://xkcd.com'
	# 如果是请求上一页的页面则把url变为上一页的url
	if prevUrl:
		turl +=  prevUrl

	# 请求页面
	res = requests.get(turl)
	# 如果请求页面出错则报错
	try:
		res.raise_for_status()
	except Exception as exc:
		print('Error: ' + str(exc))
	# 解析页面内容为html对象
	indexPage = bs4.BeautifulSoup(res.text, 'html.parser')
	# 查找页面中要下载的图片src属性，获取图片的地址
	imgElem = indexPage.select('#comic img')
	if imgElem:
		imgUrl = imgElem[0].get('src')
		# 获取图片名字
		imgName = imgUrl.split('/')[-1]

		# 拼接图片的url
		imgRes = requests.get('https:' + imgUrl)
		# 如果请求图片出错则报错
		try:
			imgRes.raise_for_status()
		except Exception as exc:
			print('Error: ' + str(exc))
		# 新建图片文件，以二进制格式写入文件，把图片放到图片文件夹
		imgFile = open(picFolder + os.path.sep + prevUrl[1:-1] + '-' + imgName, 'wb')
		for chunk in imgRes.iter_content(100000):
			imgFile.write(chunk)
		imgFile.close()

	# 获取页面的上一页 prev元素，取出上一页的url后缀
	prevElem = indexPage.select('.comicNav a')
	# prevUrl = prevElem[1].get('href')
	if prevElem:
		return prevElem[1].get('href')
	else:
		return None
	
prevUrl = ''
while True:
	prevUrl = downloadPicture(prevUrl)
	if prevUrl == '/1/':
		print('Done!')
		break
