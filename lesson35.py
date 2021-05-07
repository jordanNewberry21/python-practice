# debugging: the raise and assert statements

#raise Exception('This is the error message')
# this returns an exception object that is raised


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2')
    print(symbol * width)

    for i in range (height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 12, 5)
boxPrint('0', 2, 6)
boxPrint('9', 15, 5)
boxPrint('**', 15, 1)
boxPrint('1', 15, 5)

