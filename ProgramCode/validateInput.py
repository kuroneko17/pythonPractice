# validateInput.py

while True:
	print('Enter your age:')
	age = input()
	if age.isdecimal():
		break
	print('Please enter a number of your age.')

while True:
	print('Enter the passcode:(letters and numbers only)')
	passcode = input()
	if passcode.isalnum():
		break
	print('Passcode can only have letters and numbers.')