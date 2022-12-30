# provide list of values to format
lst = ""

def formatListForSQLInOperator(lst):
    chrInLine = 6
    lstAsString = ''.join(lst)
    x = 0
    y = 0
    lenLstAsString = len(lstAsString)

    print("(", end = '')
    for i in lstAsString:
        if x == 0:
            print("'" + i,end='')
            x += 1
            y += 1
            continue
        elif y == lenLstAsString-1:
            print("')")
        elif x % chrInLine == 0:
            print("',",end='')
            x = 0
        else:
            print(i,end='')
            x += 1
        y += 1

formatListForSQLInOperator(lst)
