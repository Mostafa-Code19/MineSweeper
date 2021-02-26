
import logging, time
logging.basicConfig(level=logging.DEBUG, format='log: %(message)s')
# logging.disable(logging.CRITICAL)
def log(code):
    logging.debug(code)


playgroundBefore = ['221', '?*?', '???']
# playground = ['122', '?*?', '?2?']  # = 122 S** S2S
# playground = ['?3*', '*6*', '***']
playground = ['221', '?*?', '???']  # 221 **S SSS
# playground = ['2?1', '?21', '11*']
# playground = ['3?2', '??2', '221']
# playground = ['1?2', '12*', '1?2']
# playground = ['1?1', '222', '1?1']
# playground = ['???', '?2?', '???']

x = 3
y = 3
playgroundsize = [x, y]

def solve():
    for row in range(y):
        for column in range(x):
            element = playground[row][column]
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
        checkAround(element, elementAround, row)

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
                cornerApply = TRBLType.get(positionType)
                elementAround.append(cornerApply)
        
        log(f'elementAround: {elementAround}')
        checkAround(element, elementAround, row)

    else:  # All around the center
        log(f'enter central')
        for moveY in (1, 0, -1):
            for moveX in (1, 0, -1):
                log(f'positionType: {row} {column} {moveY} {moveX}')
                element = playground[moveY][moveX]
                elementAround.append(element)
        log(f'elementAround: {elementAround}')
        checkAround(element, elementAround, row)

def corner(row, column):
    log('enter corner')
    if row == 0 and column == 0: return 'TopLeft'
    elif row == 0 and column == x - 1: return 'TopRight'
    elif row == x - 1 and column == 0: return 'BottomLeft'
    elif row == x - 1 and column == y - 1: return 'BottomRight'
    else: return False

def TRBL(row, column):
    log('enter TRBL')
    log(f'TRBL: {row} {column}')
    if column == 0: return 'Left'
    elif column == x - 1: return 'Right'
    elif row == 0: return 'Top'
    elif row == y - 1: return 'Bottom'
    else: return False

def checkAround(element, elementAround, row):
    log('67: enter checkAround')
    unknownCounter = elementAround.count('?')
    if not unknownCounter:
        return
    unknownIndex = elementAround.index('?')
    bombCounter = elementAround.count('*')
    log(f'number of ?: {unknownCounter} |  Index of ?: {unknownIndex} | number of *: {bombCounter}')

    if element == '?': return False

    elif element == '1':
        if unknownCounter == 1 and bombCounter == 0:
            addSolution(row, unknownCounter, solution = '*')
        elif bombCounter:
            addSolution(row, unknownCounter, solution = 'S')
        else:
            log('There is an error in checkAround !!!!!!!!!!!!!!!!')

    elif element == '2':
        if unknownCounter and bombCounter:
            addSolution(row, unknownCounter, solution = '*')
        elif unknownCounter == 2:
            addSolution(row, unknownCounter, solution = '*')
        elif bombCounter == 2:
            log(f'holllllla entering for 2 bomb - element: {element} row: {row}')
            addSolution(row, 8, solution = 'S')
        else:
            print('There is an error in checkAround')

    elif element == '3':
        if unknownCounter == 3 and bombCounter == 0:
            addSolution(row, 8, solution = '*')
        elif unknownCounter == 2 and bombCounter:
            addSolution(row, unknownCounter, solution = '*')
        elif unknownCounter and bombCounter == 2:
            addSolution(row, unknownCounter, solution = '*')
        elif bombCounter == 3:
            addSolution(row, 8, solution = 'S')
        else:
            log('There is an error in checkAround')

    else: return 'The element bigger than 3'

def addSolution(row, unknownToAdd, solution):
    if row == 0:
        for moveY in range(2):
            newRow = playground[row + moveY].replace('?', solution, unknownToAdd)
            playground[row + moveY] = newRow
            log(f'144: newRow: {newRow}')
    elif row == y - 1:
        for moveY in range(2):
            newRow = playground[row - moveY].replace('?', solution, unknownToAdd)
            playground[row - moveY] = newRow
            log(f'149: newRow: {newRow}')
    else:
        for move in (-1, 0, 1):
            newRow = playground[row - move].replace('?', solution, unknownToAdd)
            playground[row - move] = newRow
            log(f'149: newRow: {newRow}')
    return

def solved():
    end = time.time()
    solvedIn = str(end - start)
    rows = len(playground)
    print('###############################################')
    print('____Before____')
    for i in range(rows):
        print(playgroundBefore[i])
    print('____After____')
    for i in range(rows):
        print(playground[i])
    print(f'############---Solved In: {solvedIn}---###################')

start = time.time()
print(solve())