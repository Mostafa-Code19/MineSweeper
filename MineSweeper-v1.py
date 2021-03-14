
import logging, time
logging.basicConfig(level=logging.DEBUG, format='log: %(message)s')
logging.disable(logging.CRITICAL)


playgroundBefore = ['?*1', '*?1', '??1']
# playground = ['122', '?*?', '?2?']  # = 122 S** S2S
# playground = ['?3*', '*6*', '***']
# playground = ['221', '?*?', '???']  # 221 **S SSS
# playground = ['2?1', '?2S', '11*']
# playground = ['2*1', '*2S', '11*']
# playground = ['3?2', '??2', '221']
playground = ['?*1', '*?1', '??1']
# playground = ['1?1', '222', '1?1']
# playground = ['???', '*2*', '???']
# playground = ['*?1', '??1','?*1', '122', 'S1*', 'S12', '?*1']

x = 3
y = 3
playgroundsize = [x, y]

def start():
    for repeat in range(x * y):
        solve()
    solved()
    return '-----------------------'

def solve():
    for row in range(y):
        for column in range(x):
            element = playground[row][column]
            AnalyzeAround(element, row, column)

def AnalyzeAround(element, row, column):
    elementAround = []
    if corner(row, column):
        positionType = corner(row, column)
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
        
        checkAround(element, elementAround, row)

    # elif TRBL(row, column):
        positionType = TRBL(row, column)
        for move in range(2):
            for moveOpposite in (1, 0, -1):
                if positionType == 'Top': cornerApply = playground[row + move][column - moveOpposite]
                elif positionType == 'Right': cornerApply = playground[row - moveOpposite][column - move]
                elif positionType == 'Bottom': cornerApply = playground[row - move][column - moveOpposite]
                elif positionType == 'Left': cornerApply = playground[row - moveOpposite][column + move]
                elementAround.append(cornerApply)
        
        checkAround(element, elementAround, row)

    else:  # Central
        for moveY in (1, 0, -1):
            for moveX in (1, 0, -1):
                applyElement = playground[moveY][moveX]
                elementAround.append(applyElement)
        checkAround(element, elementAround, row)

def corner(row, column):
    if row == 0 and column == 0: return 'TopLeft'
    elif row == 0 and column == x - 1: return 'TopRight'
    elif row == x - 1 and column == 0: return 'BottomLeft'
    elif row == x - 1 and column == y - 1: return 'BottomRight'
    else: return False

def TRBL(row, column):
    if column == 0: return 'Left'
    elif column == x: return 'Right'
    elif row == 0: return 'Top'
    elif row == y: return 'Bottom'
    else: return False

def checkAround(element, elementAround, row):
    unknownCounter = elementAround.count('?')
    bombCounter = elementAround.count('*')
    if not unknownCounter:
        if element == 'S':
            uncoverTheSafePoint(row, str(bombCounter))
        else: return f'There is not S and Not ?'
    else:
        unknownIndex = elementAround.index('?')

        if element == '1':
            if unknownCounter == 1 and bombCounter == 0:
                addSolution(row, unknownCounter, solution = '*')
            elif bombCounter == 1:
                addSolution(row, unknownCounter, solution = 'S')
            else:
                print('There is an error in checkAround: 101')

        elif element == '2':
            if unknownCounter == 1 and bombCounter == 1:
                addSolution(row, unknownCounter, solution = '*')
            elif unknownCounter == 2:
                addSolution(row, unknownCounter, solution = '*')
            elif bombCounter == 2:
                addSolution(row, 8, solution = 'S')
            else:
                print('There is an error in checkAround: 111')

        elif element == '3':
            if unknownCounter == 3 and bombCounter == 0:
                addSolution(row, 8, solution = '*')
            elif unknownCounter == 2 and bombCounter == 1:
                addSolution(row, unknownCounter, solution = '*')
            elif unknownCounter == 1 and bombCounter == 2:
                addSolution(row, unknownCounter, solution = '*')
            elif bombCounter == 3:
                addSolution(row, 8, solution = 'S')
            else:
                print('There is an error in checkAround: 123')

        else: return 'The element bigger than 3'

def addSolution(row, unknownToAdd, solution):
    if row == 0:
        for moveY in range(2):
            newRow = playground[row + moveY].replace('?', solution, unknownToAdd)
            playground[row + moveY] = newRow
    elif row == y - 1:
        for moveY in range(2):
            newRow = playground[row - moveY].replace('?', solution, unknownToAdd)
            playground[row - moveY] = newRow
    else:
        for move in (-1, 0, 1):
            newRow = playground[row - move].replace('?', solution, unknownToAdd)
            playground[row - move] = newRow
def uncoverTheSafePoint(row, bombCounter):
        if row == 0:
            for moveY in range(2):
                newRow = playground[row + moveY].replace('S', bombCounter, 8)
                playground[row + moveY] = newRow
        elif row == y - 1:
            for moveY in range(2):
                newRow = playground[row - moveY].replace('S', bombCounter, 8)
                playground[row - moveY] = newRow
        else:
            for move in (-1, 0, 1):
                newRow = playground[row - move].replace('S', bombCounter, 8)
                playground[row - move] = newRow

def bombscounter():
    return

def solved():
    timerEnd = time.time() * 1000 # in milliseconds
    solvedIn = str(timerEnd - timerStart)[:5]
    rows = len(playground)
    print(f'________________Solved In: {solvedIn}________________')
    print('____Before____')
    for i in range(rows):
        print(playgroundBefore[i])
    print('____After____')
    for i in range(rows):
        print(playground[i])

timerStart = time.time() * 1000  # in milliseconds
print(start())