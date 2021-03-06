
import logging, time
logging.basicConfig(level=logging.DEBUG, format='log: %(message)s')
logging.disable(logging.CRITICAL)
def log(code):
    logging.debug(code)


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
            # AnalyzeAround(element, row, column)



# check around



def checkAround(element, elementAround, row):
    log('67: enter checkAround')
    unknownCounter = elementAround.count('?')
    bombCounter = elementAround.count('*')
    if not unknownCounter:
        if element == 'S':
            log(f'GG BROTHER -------------------------------------')
            uncoverTheSafePoint(row, str(bombCounter))
        else: return f'There is not S and Not ?'
    else:
        unknownIndex = elementAround.index('?')
        log(f'number of ?: {unknownCounter} |  Index of ?: {unknownIndex} | number of *: {bombCounter}')

        if element == '1':
            if unknownCounter == 1 and bombCounter == 0:
                addSolution(row, unknownCounter, solution = '*')
            elif bombCounter == 1:
                addSolution(row, unknownCounter, solution = 'S')
            else:
                log('There is an error in checkAround !!!!!!!!!!!!!!!!')

        elif element == '2':
            if unknownCounter == 1 and bombCounter == 1:
                addSolution(row, unknownCounter, solution = '*')
            elif unknownCounter == 2:
                addSolution(row, unknownCounter, solution = '*')
            elif bombCounter == 2:
                addSolution(row, 8, solution = 'S')
            else:
                print('There is an error in checkAround')

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
def uncoverTheSafePoint(row, bombCounter):
        if row == 0:
            for moveY in range(2):
                newRow = playground[row + moveY].replace('S', bombCounter, 8)
                playground[row + moveY] = newRow
                log(f'144: newRow: {newRow}')
        elif row == y - 1:
            for moveY in range(2):
                newRow = playground[row - moveY].replace('S', bombCounter, 8)
                playground[row - moveY] = newRow
                log(f'149: newRow: {newRow}')
        else:
            for move in (-1, 0, 1):
                newRow = playground[row - move].replace('S', bombCounter, 8)
                playground[row - move] = newRow
                log(f'149: newRow: {newRow}')

def bombscounter():
    return

def solved():
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
    # print(f'________________{bombCounter}Bombs Detected________________')

timerStart = time.time()
print(start())