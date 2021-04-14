# characterCount.py

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

# for chatacter in message:
# 	count.setdefault(chatacter, 0)
# 	if count.get(chatacter) != None:
# 		count[chatacter] += 1
# print(count)


for character in message: 
    count.setdefault(character, 0) 
    count[character] = count[character] + 1 
 
print(count)