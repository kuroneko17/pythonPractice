# sameName3.py
def spam(): 
 	global eggs 
 	eggs = 'spam' # this is the global 
 
def bacon(): 
	eggs = 'bacon' # this is a local 
def ham(): 
	print(eggs) # this is the global 
 
eggs = 42 # this is the global 
spam() 
print(eggs)

###
# 	在 spam()函数中，eggs 是全局 eggs 变量，因为在函数的开始处，有针对 eggs
# 变量的 global 语句。在 bacon()中，eggs 是局部变量，因为在该函数中有针对它的赋值语句。在 ham()中，eggs 是全局变量，因为在这个函数中，既没有赋值语句，也没有针对它的 global 语句。如果运行 sameName3.py，输出将是： 
 
# spam 

#  在一个函数中，一个变量要么总是全局变量，要么总是局部变量。函数中的代码没有办法先使用名为 eggs 的局部变量，稍后又在同一个函数中使用全局 eggs 变量。 如果想在一个函数中修改全局变量中存储的值，就必须对该变量使用 global语句。 
###
