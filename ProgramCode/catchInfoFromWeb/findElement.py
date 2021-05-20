# findElement.py

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com/')
# browser.get('http://bing.com')
try:
	# elem = browser.find_element_by_class_name('bookcover')
	# elem = browser.find_element_by_class_name('logo_cont')
	print('Found {} element with that class name.'.format(elem.tag_name))
	# clickElem = browser.find_element_by_link_text('Read It Online.')
except Exception as Exc:
	print(str(Exc))