def showTheRows(round):
    rows = round.split('|')
    numberOfRows = len(rows)
    for row in range(numberOfRows):
        print(rows[row])
    return ''
try: 
    print(showTheRows('*2*|32*'))

except Exception as e:
    print(e)