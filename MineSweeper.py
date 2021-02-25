
import logging
logging.basicConfig(level=logging.DEBUG, format='log: %(message)s')
# logging.disable(logging.CRITICAL)
def log(code):
    logging.debug(code)


playgroundBefore = ['2?1', '?21', '11S']
# playground = ['122', '?*?', '?2?']  # = 122 S** S2S
# playground = ['?3*', '*6*', '***']
# playground = ['221', '?*?', '???']  # 221 **S SSS
playground = ['2?1', '?21', '11S']
# playground = ['3?2', '2?2', '221']
# playground = ['1?2', '12*', '1?2']
# playground = ['1?1', '222', '1?1']


x = 3
y = 3
playgroundsize = [x, y]

def solve():
    for element in range(1, 2):
        for row in range(y):
            for column in range(x):
                element = playground[row][column]
                log(f'element:{element}, row:{row}, column:{column}')
                AnalyzeAround(element, row, column)
    
    log('going to end')
    return solved()

def AnalyzeAround(element, row, column):
    log(f'enter AnalyzeAround with element: {element}, row: {row}, column: {column}')        
    elementAround = []
    whichCorner = corner(row, column)
    log(f'Whichcorner: {whichCorner}')
    
    if whichCorner != False:
        for row in range(2):
            for column in range(2):
                cornerType = {
                    'TopLeft' : playground[row][column],
                    'TopRight' : playground[row][x - column - 1],
                    'BottomLeft' : playground[y - row - 1][column],
                    'BottomRight' : playground[y - row - 1][x - column - 1]
                }
                cornerApply = cornerType[whichCorner]
                elementAround.append(cornerApply)
        
        log(f'elementAround: {elementAround}')
        checkAround(element, elementAround, whichCorner)

    else:
        print('Not Corner')\

def corner(row, column):
    log('enter corner')
    if row == 0 and column == 0: return 'TopLeft'
    elif row == 0 and column == x - 1: return 'TopRight'
    elif row == x - 1 and column == 0: return 'BottomLeft'
    elif row == x - 1 and column == y - 1: return 'BottomRight'
    else: return False

def checkAround(element, elementAround, where):
    log('67: enter checkAround')
    unknownCounter = elementAround.count('?')
    if not unknownCounter:
        return
    unknownIndex = elementAround.index('?')
    bombCounter = elementAround.count('*')
    log(f'number of ?: {unknownCounter} |  Index of ?: {unknownIndex} | number of *: {bombCounter}')

    if element == '1':
        if unknownCounter == 1 and bombCounter == 0:
            addSolution(where, unknownCounter, solution = '*')
        elif bombCounter:
            addSolution(where, unknownCounter, solution = 'S')
        else:
            log('There is an error in checkAround !!!!!!!!!!!!!!!!')

    elif element == '2':
        if unknownCounter and bombCounter:
            addSolution(where, unknownCounter, solution = '*')
        elif unknownCounter == 2:
            addSolution(where, unknownCounter, solution = '*')
        elif bombCounter == 2:
            addSolution(where, 8, solution = 'S')
        else:
            log('There is an error in checkAround')

    elif element == '3':
        if unknownCounter == 3 and bombCounter == 0:
            addSolution(where, 8, solution = '*')
        elif unknownCounter == 2 and bombCounter:
            addSolution(where, unknownCounter, solution = '*')
        elif unknownCounter and bombCounter == 2:
            addSolution(where, unknownCounter, solution = '*')
        elif bombCounter == 3:
            addSolution(where, 8, solution = 'S')
        else:
            log('There is an error in checkAround')

    else: return 'The element bigger than 3'

def addSolution(where, unknownToAdd, solution):
    if where == 'TopLeft':
        for row in range(2):
            for column in range(2):
                if playground[row][column] == '?':
                    newRow = playground[row].replace('?', solution, unknownToAdd)
                    playground[row] = newRow

    elif where == 'TopRight':
        for row in range(2):
            for column in range(2):
                if playground[row][x - column - 1] == '?':
                    newRow = playground[row].replace('?', solution, unknownToAdd)
                    playground[row] = newRow
        log(f'115: newRow: {newRow}')

    elif where == 'BottomLeft':
        for row in range(2):
            for column in range(2):
                if playground[y - row - 1][column] == '?':
                    newRow = playground[y - row - 1].replace('?', solution, unknownToAdd)
                    playground[y - row - 1] = newRow
        log(f'137: newRow: {newRow}')

    elif where == 'BottomRight':
        for row in range(2):
            for column in range(2):
                if playground[y - row - 1][x - column - 1] == '?':
                    newRow = playground[y - row - 1].replace('?', solution, unknownToAdd)
                    playground[y - row - 1] = newRow
        log(f'152: newRow: {newRow}')
    return

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