# boxPrint.py
# symbol -> 符号，width -> 宽度，height -> 高度
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string!')
    if width <= 2:
        raise Exception('Width must be greater than 2!')
    if height <= 2:
        raise Exception('Height must be  greater than 2!')

    # 打印盒子，首位两行，中间留空
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)


    # boxPrint('*', 2, 4)
for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 33, 3)):
    # 每次循环捕捉异常，抛出
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception hanpened: ' + str(err))

