
# The purpose of this script is to format a list of values for use in the SQL In operator.
# Prior to executing the script, do the following:
# 1. Update the lst variable so that it contains the list of values that should be formatted for the SQL In operator Values should be provided in the lst variable using the following format:
    # """value1
    # value2
    # value3 """
# 2. Update the chrInLine variable indicating how many characters are in each item in lst. For the example above (value1, value2, value 3) chrInLine should be set to 6 because there are 6 characters in each item.

# Development next steps: Update script so that user is prompted to enter values for lst and chrInLine instead of having to hard code it into the script.

# ---> UPDATE VARIABLE BELOW BEFORE RUNNING <---
lst = """value1
value2
value3 """

def formatListForSQLInOperator(lst):
# ---> UPDATE VARIABLE BELOW BEFORE EXECUTING <---
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
