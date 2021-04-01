# sameName2.py

def spam():
	global eggs
	eggs = 'spam local'
	print(eggs)

eggs = 'global'
spam()
print(eggs)