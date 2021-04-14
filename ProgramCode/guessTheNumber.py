# guessTheNumber.py

import random
#	From ramdom import *

def myNumber(num,theNum,times):
	if num == theNum :
		print('Bingo!!!you guess the number,the number is ' + str(theNum) + ' .And you guess the number in ' + str(times) + ' guesses')
		return True
	elif num < theNum:
		print('Your guess is too low.Maybe try again?')
		# if num < minNum:
		# 	print('The number is between {} and {}'.format(minNum,maxNum))
		# elif num > minNum:
		# 	a
	elif num > theNum:
		print('You guess is too big.Maybe try again?')

theNumber = random.randint(1,123)
print('I am thinking of a number between 1 and 123.')
print('Take a guess.')
minNum = 0
maxNum = 123
times = 0
while True:
	inputNumber = int(input('Please type the number:'))
	times += 1
	if myNumber(inputNumber,theNumber,times):
		break