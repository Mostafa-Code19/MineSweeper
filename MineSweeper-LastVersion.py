# Base packages and code
import logging, time
logging.basicConfig(level=logging.DEBUG, format='log: %(message)s')
# logging.disable(logging.CRITICAL)
def log(code):
    logging.debug(code)

playgroundBefore = [
    '..1??',
    '.12??',
    '.1???',
    '12???',
    '?????'
]

# playground = [
#     '?11?21',
#     '2?2*?1',
#     '*2?32?',
#     '121?S?',
# ]

playground = [
    '..1??',
    '.12??',
    '.1???',
    '12???',
    '?????'
]

# Variables
x = 5
y = 5
playgroundsize = [x, y]
maxAround = 8


# Code
def startSolving(playground): #! make changes in here
    for row in range(y):
        for column in range(x):
            element = playground[row][column]
            AnalyzeAround(element, row, column)


def AnalyzeAround(element, row, column):
    elementAround = []
    try:
        print(f'the element position: {row, column}')
        for moveX in range(-1, 2):
            for moveY in range(-1, 2):
                if row + moveY >= 0 and column + moveX >= 0:
                    log(f'row: {row}, column: {column}, moveY: {moveY}, moveX: {moveX}, final position: {row + moveY, column + moveX}')
                    readingTheAround = playground[row + moveY][column + moveX]
                    elementAround.append(readingTheAround)

    except Exception:
        log(f'out of the board')
        pass

    log(f'The element around of {row, column}: {elementAround}')
    putAnswer(element, elementAround, row)


def putAnswer(element, elementAround, row):
    unknownCounter = elementAround.count('?')
    bombCounter = elementAround.count('*')

    log(f'61: enter putAnswer')
    log(f'element: {element} | number of ?: {unknownCounter} | number of *: {bombCounter}')

    if not unknownCounter:
        if element == 'S':
            addSolution('S', row, str(bombCounter))
        elif unknownCounter == 0 and bombCounter == 0:
            addSolution('S', row, '.')

        else: return f'There is not S and Not ?'
        
    else:
        if element == '1':
            if unknownCounter == 1 and bombCounter == 0:
                addSolution('?', row, '*')
            elif bombCounter == 1:
                addSolution('?', row, 'S')
            else:
                log('There is an option that not include in check around of 1')
                
        elif element == '2':
            if (unknownCounter == 1 and bombCounter == 1 or
                unknownCounter == 2 and bombCounter == 0) :
                addSolution('?', row, '*')
            elif bombCounter == 2:
                addSolution('?', row, 'S')
            else:
                log('There is an option that not include in check around of 2')

        elif element == '3':
            if (unknownCounter == 3 and bombCounter == 0 or 
                unknownCounter == 2 and bombCounter == 1 or
                unknownCounter == 1 and bombCounter == 2) :
                addSolution('?', row, '*')

            elif bombCounter == 3:
                addSolution('?', row, 'S')
            
            else:
                log('There is an option that not include in check around of 3')
        
        elif element == '?':
            if unknownCounter == 1:
                addSolution('?', row, str(bombCounter))

        else: print('just 1, 2 and 3 is available')


def addSolution(type, row, solution):
    for moveXY in range(-1, 2):
        try:
            if row + moveXY >= 0:
                newRow = playground[row - moveXY].replace(type, solution, maxAround)
                playground[row - moveXY] = newRow

        except IndexError:
            pass


def result():
    timerEnd = time.time()
    solvedIn = str(timerEnd - timerStart)
    rows = len(playground)
    print(f'________________Solved In: {solvedIn}________________')
    print('____Before____')
    for i in range(rows):
        print(playgroundBefore[i])
    print('____After____')
    for i in range(rows):
        print(playground[i])

timerStart = time.time()

try:
    # playgroundXY = str(input('Enter the Y and X numbers: Ex: 3x3 \n'))
    # playgroundXY = playgroundXY.split('x')
    # y = int(playgroundXY[0]); x = int(playgroundXY[1])
    
    # for y in range(y):
    #     elementForPlayground = str(input(f'enter the number {y + 1} row:  Ex: 1*? \n'))
    #     playground.append(elementForPlayground)
    #     playgroundBefore.append(elementForPlayground)

    startSolving(playground)

    result()

except Exception as err:
    print(err)