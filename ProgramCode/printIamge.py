# printIamge.py

# 你可以认为 grid[x][y]是一幅“图”在 x、y 坐标处的字符，
# 该图由文本字符组成。原点(0, 0)在左上角，向右 x 坐标增加，向下 y 坐标增加。 
# 复制前面的网格值，编写代码用它打印出图像。 
grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']]
for y in range(0, len(grid[0])):
	for x in range(0, len(grid)):
		print(grid[x][y],end = '')
	print()
# for x in grid:
# 	for y in x:
# 		print()