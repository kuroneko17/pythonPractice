# aotuPlay2048.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get(' https://gabrielecirulli.github.io/2048/')
try:
	elem = browser.find_element_by_tag_name('html')
	times = 0 
	while True:
		elem.send_keys(Keys.UP)
		elem.send_keys(Keys.RIGHT)
		elem.send_keys(Keys.DOWN)
		elem.send_keys(Keys.LEFT)
		if times == 100000:
			break
		times += 1
except:
	print('Cant find that element.')