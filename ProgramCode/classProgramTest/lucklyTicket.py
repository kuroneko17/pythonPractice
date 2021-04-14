# lucklyTicket.py

# 可以从01-35共35个号码中，选取5个号码为前区号码，并从01-12共12个号码中选取2个号码为后区号码 

import random

# 返回数字列表
def getNumList(end, start = 0):
	numList = []
	for i in range(start, end):
		i += 1
		if i < 10:
			i = '0' + str(i)
		numList.append(str(i))
	return numList

# 生成随机号码
def getRandomNum(numList, times):
	# 重新复制numList 的值给tempNumList，避免函数操作修改numList
	tempNumlist = numList[:]
	random.shuffle(tempNumlist)
	randomNum = ''
	for i in range(times):
		randNum = random.choice(tempNumlist)
		randomNum += randNum + ' '
		tempNumlist.remove(randNum)
		random.shuffle(tempNumlist)
	return randomNum

# 前面的选取号码
numFrList = getNumList(35)
# 后面的选取号码
numBeList = getNumList(12)

# 生成中奖号码
lucklyTicketNum = ''
lucklyTicketNum = getRandomNum(numFrList, 5)
lucklyTicketNum += getRandomNum(numBeList, 2)
print('The luckly number is {}.'.format(lucklyTicketNum))

# 次数
times = 0
while True:
	# 生成自己的号码
	myNum = ''
	myNum = getRandomNum(numFrList, 5)
	myNum += getRandomNum(numBeList, 2)

	times += 1
	if myNum == lucklyTicketNum:
		print('Jcakpot!!!Your number "{}" is the luckly ticket number.'.format(myNum))
		print('times: {}'.format(times))
		break

	if times == 100000:
		print('Sorry, sad your are miss the price.')
		print('times: {}'.format(times))
		break

