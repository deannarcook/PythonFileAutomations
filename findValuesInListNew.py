def formatListForSQLInOperator(lst, charsInListItem):
    chrInLine = charsInListItem
    lstAsString = ''.join(lst)
    x = 0
    y = 0
    lenLstAsString = len(lstAsString)

    newLst = ()
    # print("(", end = '')
    for i in lstAsString:
        if x == 0:
            lstItem = "'" + i
            x += 1
            y += 1
            continue
        elif y == lenLstAsString - 1:
            lstItem += "'"
        elif x % chrInLine == 0:
            lstItem += "'"
            newLst.append(lstItem)
            x = 0
        else:
            lstItem += i
            x += 1
        y += 1


# values to search for - provide list of string values with no single quotes and no commas
searchValues = ()

print("Checking if values exist in list.")

formatListForSQLInOperator(searchValues, 6)

formatListForSQLInOperator(searchList, 6)

for i in searchValues:
    # print(i + " ",end='')
    if i not in searchList:
        print(i + " does not exist in list")
    # if i in searchList:
    #    print("exists in list")
    # else:
    #    print("does not exist in list")

print("script execution complete")
