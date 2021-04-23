# coinFlip.py

""""
调试硬币抛掷
下面程序的意图是一个简单的硬币抛掷猜测游戏。玩家有两次猜测机会（这
是一个简单的游戏） 。但是，程序中有一些缺陷。让程序运行几次，找出缺陷，使
该程序能正确运行。 
"""
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,format=' %(asctime)s - %(levelname)s -%(message)s ' )
# logging.disable(logging.ERROR)
# logging.disable(logging.CRITICAL)

import sys, random

# spam = 1
# assert spam >= 10, 'AsserttionError'

def eggsAndBacon(eggs, bacon):
	assert not eggs.lower() == bacon.lower(), 'AssertionError'
	# assert False, 'Always throw AssertionError'

def coinFlip():
	coinSide = ('head', 'tail')
	# 0 is the head, 1 is the tail
	toss = random.randint(0, 1)

	for i in range(2):
		guess = ''
		while guess not in coinSide:
			print('Guess the coin toss! Enter head or tail: ')
			guess = input()

		if guess == coinSide[toss]:
			print('Bingo.You got it.')
			sys.exit()
		else:
			print('Nope! Guess again.')
	print('Sorry,you have no chance, the coin toss is {}.'.format(coinSide[toss]))

coinFlip()
# eggsAndBacon('abcDEf', 'AbcDef')
