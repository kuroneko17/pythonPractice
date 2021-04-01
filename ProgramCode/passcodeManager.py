#! python3
# passcodeManager.py  - A insecure passcode locker progarm
# 口令管理器

"""
	你可能在许多不同网站上拥有账号，每个账号使用相同的口令是个坏习惯。
	如果这些网站中任何一个有安全漏洞，黑客就会知道你所有的其他账号的口令。
	最好是在你的计算机上，使用口令管理器软件，利用一个主控口令，
	解锁口令管理器然后将某个账户口令拷贝到剪贴板，再将它粘贴到网站的口令输入框。 
	你在这个例子中创建的口令管理器程序并不安全，但它基本展示了这种程序的工作原理。 
"""
"""
				项目编写方式
	第 1 步：程序设计和数据结构 
	第 2 步：处理命令行参数
	第 3 步：复制正确的口令 
"""

import sys
import pyperclip

passcodes = {
						'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6', 
						'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt', 
						'luggage': '12345'
					}

if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

# first command line arg is the account name
account = sys.argv[1]

if account not in passcodes.keys():
	print('There is no account named {}'.format(account))
	sys.exit()
else:
	pyperclip.copy(passcodes[account])
	print('Passcode for {} copied to clipboard.'.format(account))