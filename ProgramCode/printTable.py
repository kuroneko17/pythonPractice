#! python3
# printTable.py

"""
	编写一个名为 printTable()的函数，它接受字符串的列表的列表，将它显示在组
	织良好的表格中， 每列右对齐。假定所有内层列表都包含同样数目的字符串。例如，
	该值可能看起来像这样：
	 apples Alice dogs 
	 oranges Bob    cats 
	cherries Carol moose 
	  banana David goose 
"""
def printTable(tableList):
	# tableList[0][0] tableList[1][0]
	# tableList[0][1]
	lengthList = []
	for i in tableList:
		length = 0
		for j in i:
			if len(j) > length:
				length = len(j)
		lengthList.append(length)
	for i in range(0, len(tableList[0])):
		for j in range(0, len(tableList)):
			print(tableList[j][i].rjust(lengthList[j]), end = ' ')
			# print(tableList[j][i], end = ' ')
		print()


tableData = [
						['apples', 'oranges', 'cherries', 'banana'], 
						['Alice', 'Bob', 'Carol', 'David'], 
						['dogs', 'cats', 'moose', 'goose']
					] 
printTable(tableData)
