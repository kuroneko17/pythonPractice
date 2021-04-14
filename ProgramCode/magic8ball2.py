# magic8ball2.py

import random
#	From random inport *

def getAnswer(answerNumber):
	answerNumber -= 1
	answer = [
	'It is certain', 
	'It is decidedly so', 
	'Yes', 
	'Reply hazy and try again', 
	'Ask again later', 
	'Concentrate and ask again', 
	'My reply is no', 
	'Outlook not so good', 
	'Very doubtful'
	]
	return answer[answerNumber]

theNumber = random.randint(1,9)
fortune =  getAnswer(theNumber)
print(fortune)
