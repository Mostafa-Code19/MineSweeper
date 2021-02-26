
import logging
logging.basicConfig(level=logging.DEBUG, format='log: %(message)s')
# logging.disable(logging.CRITICAL)
def log(code):
    logging.debug(code)


playgroundBefore = ['1?1', '222', '1?1']
# playground = ['122', '?*?', '?2?']  # = 122 S** S2S
# playground = ['?3*', '*6*', '***']
# playground = ['221', '?*?', '???']  # 221 **S SSS
# playground = ['2?1', '?21', '11*']
# playground = ['3?2', '??2', '221']
# playground = ['1?2', '12*', '1?2']
playground = ['1?1', '222', '1?1']

x = 3
y = 3
playgroundsize = [x, y]

def solve():
    for repeatTheCheck in range(round(len(playground) / 2)) :
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
    if corner(row, column):
        positionType = corner(row, column)
        log(f'positionType: {positionType} {row} {column}')
        for moveY in range(2):
            for moveX in range(2):
                cornerType = {
                    'TopLeft' : playground[moveX][moveY],
                    'TopRight' : playground[moveX][x - moveY - 1],
                    'BottomLeft' : playground[y - moveX - 1][moveY],
                    'BottomRight' : playground[y - moveX - 1][x - moveY - 1]
                }
                cornerApply = cornerType[positionType]
                elementAround.append(cornerApply)
        
        log(f'elementAround: {elementAround}')
        checkAround(element, elementAround, positionType)

    elif TRBL(row, column):
        positionType = TRBL(row, column)
        for move in range(2):
            for moveOpposite in (1, 0, -1):
                log(f'positionType: {positionType} {row} {column} {move} {moveOpposite}')
                TRBLType = {
                    'Top' : playground[row + move][column - moveOpposite], # 01 | 00 01 02 10 11 12 ok
                    'Right' : playground[row - moveOpposite][column - move], # 12 | 02 12 22 01 11 21
                    'Bottom' : playground[row - move][column - moveOpposite], # 21 | 20 21 22 10
                    'Left' : playground[row - moveOpposite][column + move], # 10 | 00 10 20 01 11 21 ok
                }
                cornerApply = TRBLType[positionType]
                elementAround.append(cornerApply)
        
        log(f'elementAround: {elementAround}')
        checkAround(element, elementAround, positionType)

def corner(row, column):
    log('enter corner')
    if row == 0 and column == 0: return 'TopLeft'
    elif row == 0 and column == x - 1: return 'TopRight'
    elif row == x - 1 and column == 0: return 'BottomLeft'
    elif row == x - 1 and column == y - 1: return 'BottomRight'
    else: return False

def TRBL(row, column):
    log('enter TRBL')
    if column == 0: return 'Left'
    elif column == x: return 'Right'
    elif row == 0: return 'Top'
    elif row == y: return 'Bottom'
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