# ticTacToe.py

# def printBoard(key, value):
# 	theBoard = {
# 							'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
# 							'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
# 							'low-L': ' ', 'low-M': ' ', 'low-R': ' '
# 						}
# 	if theBoard.get(key) != ' ':
# 		print('This localtion is already set.Please choose anther peace.')
# 		return False
# 	else:
# 		theBoard[key] = value

# 	# for i in theBoard:
# 	# 	if 'L' in i:
# 	# 		print(' | ', end = '')
# 	# 	print(i, end = ' | ')
# 	# 	if 'R' in i:
# 	# 		print()

# 	count = 1
# 	for i in theBoard:
# 		if count % 3 == 1:
# 			print('| ', end = '')
# 		print(theBoard[i], end = ' | ')
# 		if count % 3 == 0:
# 			print()
# 		count += 1

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '} 

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
	printBoard(theBoard)
	print('Turn of {}.Move on which space?'.format(turn))
	move = input()
	theBoard[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
printBoard(theBoard)
