def showTheRows(round):
    rows = round.split(' ')
    numberOfRows = len(rows)
    for row in range(numberOfRows):
        print(rows[row])
    return 'Done'

def countTheBombs(round):
    rows = round.split(' ')
    bombs = []
    for i in range(len(rows)):
        bombsOfEachRow = 0
        for j in range(3):
            eachElement = rows[i][j]
            if eachElement == '*':
                bombsOfEachRow += 1
        bombs.append(bombsOfEachRow)
    print(bombs)
    return 'Done'

def countTheunknown(round):
    rows = round.split(' ')
    unknown = []
    for i in range(len(rows)):
        unknownForEachrow = 0
        for j in range(3):
            eachElement = rows[i][j]
            if eachElement == '?':
                unknownForEachrow += 1
        unknown.append(unknownForEachrow)
    print(unknown)
    return 'Done'

def resolveTheUnknown(round):
    return

try: 
    # print(countTheBombs('121 *?* 121'))
    # print(showTheRows('121 *?* 121'))
    print(countTheunknown('121 *?* 121'))

except Exception as e:
    print(e)