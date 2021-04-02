import pprint

cat = {'name': 'Zophie', 'age': 7, 'color': 'gray'}

allCats = []

allCats.append({'name': 'Zophie', 'age': 7, 'color': 'gray'})
allCats.append({'name': 'Henry', 'age': 5, 'color': 'black'})
allCats.append({'name': 'Daisy', 'age': 3, 'color': 'tortie'})

allCats.append({'name': '???', 'age': -1, 'color': 'orange'})


print(allCats)


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}



theBoard['mid-M'] = 'X'

# writing it like this creates a new tuple that is unrelated to the dictionary
theBoard['top-L', 'top-M', 'top-R'] = 'O'

theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['mid-L'] = 'X'
theBoard['low-R'] = 'X'

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

# type function
type(42)
type(theBoard)
type('hello')
type(3.14)