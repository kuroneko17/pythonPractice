# collatz.py

def collatz(number):
	remainder = number % 2
	if remainder == 0:
		result = number // 2
		print('The number is even number and {} // 2 = {}'.format(number, result))
	elif remainder == 1:
		result = number * 3 + 1
		print('The number is odd number and {}  * 3 + 1 = {}'.format(number, result))
	return result

enterNum = int(input('Please type your number:'))
# while True:
# for i in range(1,23):
# 	result = collatz(enterNum)
# 	print(result)
# 	if result == 1:
# 		break

result =  collatz(enterNum)
time = 0
while True:
	if result == 1:
		break
	else :
		result = collatz(result)
		time += 1
print(time)