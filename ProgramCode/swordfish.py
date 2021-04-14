while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
        # break
    print('Please type the passcode.(BTW，the code is fish.)')
    passcode = input()
    if passcode == 'swordfish':
        break
print('Thank you.^0^')
