#! python3
# bulletPointAdder.py  -- A add bullet point for wiki mask program
#	向维基标记中添加无序列表

import sys
import pyperclip

"""
	1.	从剪贴板中获取文本
	2.	把获取的文本转换为列表
	3.	 处理文本(添加标记)
	4.	把处理后的文本返回到剪切板
"""
text = pyperclip.paste()
textList = text.split('\n')
for i in range(0, len(textList)):
	if i == 0:
		textList[i]  = '* ' + textList[i]
	textList[i] = textList[i] + '\n'
textReturn = '* '.join(textList)
pyperclip.copy(textReturn)

"""
#! python3 
# bulletPointAdder.py - Adds Wikipedia bullet points to the start 
# of each line of text on the clipboard. 
 
import pyperclip 
text = pyperclip.paste() 
 
# Separate lines and add stars. 
lines = text.split('\n') 
for i in range(len(lines)): # loop through all indexes for "lines" list 
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list 
text = '\n'.join(lines) 
pyperclip.copy(text
"""