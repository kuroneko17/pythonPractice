# favoriteLanguages.py
from collections import OrderedDict

"""
	这是一个很不错的类，它兼具列表和字典的主要优点（在将信息关联起来的同时保留原来的顺序）。
	等你开始对关心的现实情形建模时，可能会发现有序字典正好能够满足需求。
	随着你对标准库的了解越来越深入，将熟悉大量可帮助你处理常见情形的模块。
"""
favoriteLanguages = OrderedDict()
# print(favoriteLanguages)
favoriteLanguages['jen'] = 'python'
favoriteLanguages['sarah'] = 'c'
favoriteLanguages['edward'] = 'ruby'
favoriteLanguages['kuro'] = 'rust'
favoriteLanguages['phil'] = 'python'

for name, language in favoriteLanguages.items():
	print('{}\'s favorite language is {}.'.format(name.title(), language.title()))