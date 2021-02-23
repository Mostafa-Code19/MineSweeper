def showTheRows(round):
    rows = round.split(' ')
    numberOfRows = len(rows)
    for row in range(numberOfRows):
        print(rows[row])
    return ''

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
    return bombs

def numberOfBombsAround(round, rowStart, columnOfUnknown):
    rows = round.split(' ')
    bombs = 0
    columnRange = 3
    columnStart = 0
    if columnOfUnknown == 3:
        columnStart = 2
        columnRange = 2
    elif columnOfUnknown == 1:
        columnStart = 0
        columnRange = 2
    try:
        for readColumnTime in range(3):
            for column in range(columnRange):
                eachElement = rows[columnStart + readColumnTime][column]
                if eachElement == '*':
                    bombs += 1
    except IndexError:
        print('outOfIndex')

    return solution(bombs)

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
    # print(unknown)
    return unknown

def positionOfTheElements(round, find):                   # 1 2 1
    rows = round.split(' ')                               # * ? *
    countOfBombsInEachRow = countTheunknown(round)        # 1 2 1
    for row in range(3):
        if countOfBombsInEachRow[row] >= 1:
            for element in range(3):
                if rows[row][element] == find:
                    elementRow = row + 1
                    elementColumn = element + 1
                    print(f'The element: {elementRow}:{elementColumn}')
                    print(numberOfBombsAround(round, elementRow - 1, elementColumn))
    return 'Done'

def solution(answer):
    return f'? = {answer}' 



print(positionOfTheElements('121 *?* 121', '?'))
# try: 
#     # print(countTheBombs('121 *?* 121'))
#     # print(showTheRows('121 *?* 121'))
#     # print(countTheunknown('121 *?* 121'))
#     print(positionOfTheElements('121 *** 12?', '?'))

# except Exception as e:
#     print(e)