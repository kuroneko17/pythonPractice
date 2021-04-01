# sameName.py

def spam():
	e =  'wer2'
	print(e, end = '\n ' + '=' * 10 + '\n')
	eggs = 'spam local'
	print(eggs)

def bacon():
	eggs = 'bacon local'
	print(eggs)
	spam()
	print(eggs)

eggs = 'global'
# spam()
bacon()
print(eggs)