# factorialLog.py

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def getResult(number):
	logging.debug('Start of factorial(%s%%)' % (number))
	result = 1
	for i in range(number):
		i += 1
		result *= i
		logging.debug('i is {}, result is {}'.format(i, result))
		# logging.debug('i is ' + str(i) + ', result is ' + str(result))
	logging.debug('End of factorial(%s%%)' % (number))
	return result

print(getResult(7))
logging.debug('End of program')
"""
import logging 
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') 
logging.debug('Start of program') 
 
def factorial(n): 
     logging.debug('Start of factorial(%s%%)' % (n)) 
     total = 1 
     # for i in range(n + 1): 
     for i in range(1, n + 1): 
           total *= i 
           logging.debug('i is ' + str(i) + ', total is ' + str(total)) 
     logging.debug('End of factorial(%s%%)' % (n)) 
     return total 
 
print(factorial(5)) 
logging.debug('End of program') 
"""