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
                    print(row + 1, element + 1)
                    #! should count the bomb around

    return 'Done'

    #     for elements in range(3):
    #         unknownOfRow = row[elements]
    #         if unknownOfRow >= 1:
    #             print(row.index(row[elements]))
    return ''


try: 
    # print(countTheBombs('121 *?* 121'))
    # print(showTheRows('121 *?* 121'))
    # print(countTheunknown('121 *?* 121'))
    print(positionOfTheElements('121 *?* 121', '?'))

except Exception as e:
    print(e)