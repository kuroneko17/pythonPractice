# howAreYou1.py

"""
	请注意，这些方法没有改变字符串本身，而是返回一个新字符串。
	如果你希望改变原来的字符串，就必须在该字符串上调用 upper()或 lower()，
	然后将这个新字符串赋给保存原来字符串的变量。这就是为什么必须使用 spam = spam.upper()，
	才能改变spam 中的字符串，而不是仅仅使用 spam.upper()
	（这就好比，如果变量 eggs 中包含值 10，写下 eggs + 3 并不会改变 eggs 的值，但是 eggs = eggs + 3 会改变 egg 的值） 。 
	如果需要进行大小写无关的比较， upper()和 lower()方法就很有用。 字符串'great'和'GREat'彼此不相等。
	但在下面的小程序中，用户输入 Great、GREAT 或 grEAT 都没关系，因为字符串首先被转换成小写。
"""
print('How are you?')
response = input()
if response.lower() == 'great':
	print('I feel great too.')
else:
	print('I hope the rest of your day is good.')