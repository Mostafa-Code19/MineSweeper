
import logging
logging.basicConfig(level=logging.DEBUG, format='log: %(message)s')
logging.disable(logging.CRITICAL)
def log(code):
    logging.debug(code)


# playground = ['122', '?*?', '?2?']  # = 122 S** S2S
# playground = ['?3*', '*6*', '***']
# playground = ['221', '?*?', '???']
# playground = ['2?1', '?21', '11S']
playgroundBefore = ['3?2', '??2', '221']
playground = ['3?2', '??2', '221']


x = 3
y = 3
playgroundsize = [x, y]

def corner(row, column):
    log('enter corner')
    if row == 0 and column == 0: return 'topLeft'
    elif row == 0 and column == x: return 'upRight'
    elif row == x and column == 0: return 'downLeft'
    elif row == x and column == y: return 'downRight'
    else: return False

def AnalyzeAround(element, row, column):
    log('enter check')        
    elementAround = []
    whichCorner = corner(row, column)
    log(f'whichCorner: {whichCorner}')
    if whichCorner != False:
        log(f'corner: TRUE')
        if whichCorner == 'topLeft':
            for row in range(2):
                for column in range(2):
                    elementAround.append(playground[row][column])
            checkAround(element, elementAround, whichCorner)
    return

def checkAround(element, elementAround, where):
    log('enter checkAround')
    unknownCounter = elementAround.count('?')
    unknownIndex = (elementAround.index('?'))
    bombCounter = elementAround.count('*')
    log(f'number of ?: {unknownCounter} | number of *: {bombCounter} | Index of ?: {unknownIndex}')

    if element == '1':
        if unknownCounter == 1 and bombCounter == 0 in elementAround:
            addSolution(where, unknownCounter, solution = '*')
        elif '*' in elementAround:
            addSolution(where, unknownCounter, solution = 'S')
        else:
            log('There is an error in checkAround')

    elif element == '2':
        if unknownCounter == 1 and bombCounter == 1:
            addSolution(where, unknownCounter, solution = '*')
        elif unknownCounter == 2:
            addSolution(where, unknownCounter, solution = '*')
        elif bombCounter == 2:
            addSolution(where, 8, solution = 'S')
        else:
            log('There is an error in checkAround')

    elif element == '3':
        log(f'Entering element 3')
        if unknownCounter == 3 and bombCounter == 0:
            addSolution(where, 8, solution = '*')
        elif unknownCounter == 2 and bombCounter == 1:
            addSolution(where, unknownCounter, solution = '*')
        elif unknownCounter == 1 and bombCounter == 2:
            addSolution(where, unknownCounter, solution = '*')
        elif bombCounter == 3:
            addSolution(where, 8, solution = 'S')
        else:
            log('There is an error in checkAround')
        log('going to end')
        return solved()
    else: return 'The element bigger than 3'

def addSolution(where, unknownToAdd, solution):
    if where == 'topLeft':
        for row in range(2):
            for column in range(2):
                if playground[row][column] == '?':
                    x = playground[row].replace('?', solution, unknownToAdd)
                    playground[row] = x
    return

def solve():
    for element in range(1, 2):
        log(element)
        for row in range(y):
            for column in range(x):
                element = playground[row][column]
                log(f'element:{element}, row:{row}, column:{column}')
                AnalyzeAround(element, row, column)
    return ' '

def solved():
    rows = len(playground)
    print('###############################################')
    print('____Before____')
    for i in range(rows):
        print(playgroundBefore[i])
    print('____After____')
    for i in range(rows):
        print(playground[i])
    print('###############################################')

print(solve())