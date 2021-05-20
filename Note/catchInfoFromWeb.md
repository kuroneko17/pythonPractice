#	从web抓取信息
---
##	编写python程序抓取web上面的信息
---
*	模块
	-	webbrowser：是python自带的，打开浏览器获取指定页面
	-	urllib2：
	-	requests：从因特网上下载文件和网页
		*	requests.get(url)
		*	requests.post(url)
		```
		import requests, json
		url = 'https://www.bing.com'
		urlParams = {'key': 'value'}
		headers = {'content-type': 'application/json', user-agent': 'myapp/0.0.1'}
		cookie = {'key': 'value'}
		data = {'info': 'datas'}
		res = requests.get(url, params = urlParams, headers = headers, cookie = cookie, timeout=30)
		postRes = requests.post(url, data = json.dumps(data))
		# print(postRes.json())
		```
		*	响应(res = request.get(url, params = urlParams))
			-	res.url
			-	res.encoding(res.encoding='utf-8')
			-	res.text
			-	res.content
			-	res.headers
			-	res.status_code
			-	res.raw
			-	res.ok
			-	res.json()
			-	res.rasie_for_status()
			-	res.history
			-	res.requests.headers
		*	requests.Session()
	-	Beautiful Soup：解析HTML，即网页编写的格式
	-	selenium：启动并控制一个webbrowser，selenium能够填充表单，并模拟鼠标在这个浏览器中点击
*	使用webbrowser模块的mapIt.py()
*	使用requests模块从web下载文件
	-	requests.get(url) -- 使用requests.get()函数下载一个网页
	-	将下载的文件保存到硬盘中
	```
	>>> import webbrowser
	>>> webbrowser.open('http://inventwithpython.com/')
	True
	>>> import requests
	>>> requests.get('https://www.baidu.com')
	<Response [200]>
	>>> res = requests.get('https://www.baidu.com')
	>>> type(res)
	<class 'requests.models.Response'>
	>>> len(res.text)
	2443
	>>> print(res.text[:280])
	<!DOCTYPE html>
	<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8>
	<meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer>
	<link rel=stylesheet type=text/css href=https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/
	>>> res.status_code
	200
	>>> requests.codes.ok
	200
	>>> requests.codes
	<lookup 'status_codes'>
	>>> (requests.codes)
	<lookup 'status_codes'>
	>>> res = requests.get('https://bilibili.com')
	>>> res.raise_for_status()
	```
*	使用bs4.BeautifulSoup()函数打印html元素
	1.	导入bs4模块
	2.	获取html文件，用open()函数打开(指定编码格式)
	3.	把文件对象传给bs4.BeautifulSoup()
	4.	使用BeautifulSoup对象选择器获取指定元素
	```
	>>> import os
	>>> os.listdir(os.getcwd())
	['mapIt.py', 'testWebPage.html']
	>>> import bs4
	>>> testWeb = open('testWebPage.html')
	>>> testWebSoup = bs4.BeautifulSoup(testWeb.read())
	Traceback (most recent call last):
	  File "<console>", line 1, in <module>
	UnicodeDecodeError: 'gbk' codec can't decode byte 0xac in position 465: illegal multibyte sequence
	>>> testWeb.close()
	>>> testWeb = open('testWebPage.html', encoding='utf-8')
	>>> testWebSoup = bs4.beautifulSoup(testWeb.read())
	Traceback (most recent call last):
	  File "<console>", line 1, in <module>
	AttributeError: module 'bs4' has no attribute 'beautifulSoup'
	>>> testWebSoup = bs4.BeautifulSoup(testWeb.read())
	>>> testWebElm1 = testWebSoup.select('#nearby')
	>>> print(testWebElm1)
	[<div id="nearby">
	<span>在</span><span class="poiname">天安门...</span><span>周边搜</span>
	<input autocomplete="off" id="nearbyipt" type="text"/>
	</div>]
	>>> testWebElm2 = testWebSoup.select('span')
	>>> print(testWebElm2)
	[<span>在</span>, <span class="poiname">天安门...</span>, <span>周边搜</span>, 
	<span class="ring" id="nearbyloading"></span>, <span class="ring" id="searchloading"></span>]
	>>> testWebElm2 = testWebSoup.select('div span')
	>>> print(testWebElm2)
	```

		|  传递给select()方法的选择器   |  将匹配的元素  |
		|  -------     								|  ----			     |
		|  soup.select('div')  							|  所有名为div的元素  |
		|  soup.select('#idName')  					|  所有带id属性为idName的元素  |
		|  soup.select('.className')  				|  所有使用CSSclass属性名为className的元素  |
		|  soup.select('div span')  					|  所有在div中元素之内的span元素  |
		|  soup.select('div > span')  					|  所有直接在div元素之内的span元素，中间没有其他元素  |
		|  soup.select('input[name]')  				|  所有名为input，并且有一个属性为name，其他无所谓的元素  |
		|  soup.select('input[type="button"]')  |  所有名为input并且有个属性值为button的元素  |

	-	项目：“I’m Feeling Lucky”Google 查找(lucky.py) 
	-	项目：下载所有 XKCD 漫画 (downloadXkcd.py)
*	使用seleniumm模块控制浏览器
	-	selenium 模块让 Python 直接控制浏览器，实际点击链接，填写登录信息，几乎就像是有一个人类用户在与页面交互。
	-	from selenium import webdriver(不是import selenium， 而是要运行from selenium import webdriver) 
		*	webdriver.Firefox 
	-	在页面中寻找元素(find_element_*和find_elements_*	)
		*	find_element_*方法返回一个 WebElement 对象，代表页面中匹配查询的第一个元素。find_elements_*方法返回 WebElement_*对象的列表，包含页面中所有匹配的元素。 
		*	如果页面上没有元素匹配该方法要查找的元素，selenium模块就会抛出NoSuchElement异常。如果你不希望这个异常让程序崩溃，就在代码中添加 try 和 except 语句。
		*	selenium 的 WebDriver 方法，用于寻找元素 

			|  方法名  |  返回的webElement对象/列表  |
			|  ------ 	|   -------    |
			|  browser.find_element_by_class_name(name)				|  使用 CSS 类 name 的元素 |
			|  browser.find_elements_by_class_name(name)				|   |
			|  browser.find_element_by_css_selector(selector)   		|  匹配 CSS selector 的元素   |
			|  browser.find_elements_by_css_selector(selector)		|   |
			|  browser.find_element_by_id(id)									|  匹配 id 属性值的元素  |
			|  browser.find_elements_by_id(id)									|   |
			|  browser.find_element_by_link_text(text)					|  完全匹配提供的 text 的<a>元素  |
			|  browser.find_elements_by_link_text(text)					|   |
			|  browser.find_element_by_partial_link_text(text)		|  包含提供的 text 的<a>元素  |
			|  browser.find_elements_by_partial_link_text(text)		|   |
			|  browser.find_element_by_name(name)    						|  匹配 name 属性值的元素   |
			|  browser.find_elements_by_name(name)  	 					|   |
			|  browser.find_element_by_tag_name(name)					|  匹配标签 name 的元素(大小写无关，<a>元素匹配'a'和'A') |
			|  browser.find_elements_by_tag_name(name) 				|   |

		*	WebElement 的属性和方法 

			|  属性或方法	|  描述   |
			|  ------ 			|  -------    |
			|  tag_name  					|  标签名，例如 'a'表示<a>元素  |
			|  get_attribute(name)		|  该元素 name 属性的值  |
			|  text  							|  该元素内的文本，例如<span>hello</span>中的'hello'  |
			|  clear()  							|  对于文本字段或文本区域元素，清除其中输入的文本   |
			|  is_displayed()  				|  如果该元素可见，返回 True，否则返回 False   |
			|  is_enabled()  				|  对于输入元素，如果该元素启用，返回 True，否则返回 False   |
			|  is_selected()					|  对于复选框或单选框元素，如果该元素被选中，选择 True，否则返回 False   |
			|  location							|  一个字典，包含键'x'和'y'，表示该元素在页面上的位置  |

		*	点击页面
		```
		form selenium import webdriver
		browser  = webdriver.Firefox()
		browser.get('http://example.com')
		linkElem = browser.find_element_by_link_text('clickElem')
		linkElem.click()
		```
		*	填写并提交表单
		```
		emailElem = browser.find_element_by_id('email')
		emailElem.send_keys('myEmail@email.com')
		passwordElem = browser.find_element_by_id('password')
		passwordElem.send_keys('myPassword')
		emailElem.submit()
		```
		*	发送特殊键
		```
		from selenium.webdriver.common.keys import Keys
		htmlElem = browser.find_element_by_tag_name(html)
		htmlElem.send_keys(Keys.END)
		htmlElem.send_keys(Keys.HOME)
		``` 

			|  属性  |  含义  |
			|  ---- 	|  ---- 	|
			|  Keys.DOWN, Keys.UP, Keys.LEFT,Keys.RIGHT 						|  键盘箭头键 |
			|  Keys.ENTER, Keys.RETURN 														|  回车和换行键 |
			|  Keys.HOME, Keys.END, Keys.PAGE_DOWN,Keys.PAGE_UP   	|  Home 键、End 键、PageUp 键和 Page Down 键 |
			|  Keys.ESCAPE, Keys.BACK_SPACE,Keys.DELETE 						|  Esc、Backspace 和字母键 |
			|  Keys.F1, Keys.F2, . . . , Keys.F12 												|  键盘顶部的 F1到 F12键 |
			|  Keys.TAB 																					|  Tab 键  |

		*	点击浏览器按键
			-	browser.back()  点击返回按钮
			-	browser.forward()  点击向前按钮
			-	browser.refresh()  点击刷新页面按钮
			-	browser.quit()  点击关闭窗口按钮	

