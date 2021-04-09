# message.py

def showMessage(message):
	for msg in message:
		print(msg)
def sendMessage(message, sentMessage):
	for msg in message:
		print(msg)
		sentMessage.append(msg)

messages = ['one', 'two', 'three']
sendMessages = []
# showMessage(messages)
sendMessage(messages, sendMessages)

print('='*20+'  messages  '+'='*20)
for msg in messages:
		print(msg)
		
print('='*20+'  sendMessages  '+'='*20)
for msg in sendMessages:
		print(msg)