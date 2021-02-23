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

def numberOfBombsAround(round, elementRow, elementColumn):                      # * 6 *
                                                                                # 3 ? 3
    rows = round.split(' ')                                                     # 1 * 2
    bombs = 0
    if elementRow == 1 or elementRow == 3:
        if elementColumn == 1:
            while elementColumn <= 2:
               for i in range(2):
                    element = (rows[elementColumn - 1][i])
                    if element == '*':
                        bombs += 1
               elementColumn += 1
        elif elementColumn == 3:
            while elementColumn >= 2:
               for i in range(3):
                    element = (rows[elementColumn - 1][i])
                    if element == '*':
                        bombs += 1
               elementColumn -= 1
    else:
        for i in (elementColumn - 2, elementColumn - 1, elementColumn):
            for j in range(3):
                if rows[i][j] == '*':
                    bombs += 1

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

def positionOfTheElements(round, find):                   # 2 * ?    ? 3 *    * 6 *     
    rows = round.split(' ')                               # * 3 *    * 6 *    3 ? 3 
    countOfBombsInEachRow = countTheunknown(round)        # 1 2 1    1 2 1    1 * 2
    for row in range(3):
        if countOfBombsInEachRow[row] >= 1:
            for element in range(3):
                if rows[row][element] == find:
                    elementRow = row + 1
                    elementColumn = element + 1
                    print(f'The element: {elementRow}:{elementColumn}')
                    print(numberOfBombsAround(round, elementRow, elementColumn))
    return 'Done'

def solution(answer):
    return f'? = {answer}' 



print(positionOfTheElements('*6* 3?3 1*2', '?'))
# try: 
#     # print(countTheBombs('121 *?* 121'))
#     # print(showTheRows('121 *?* 121'))
#     # print(countTheunknown('121 *?* 121'))
#     print(positionOfTheElements('121 *** 12?', '?'))

# except Exception as e:
#     print(e)