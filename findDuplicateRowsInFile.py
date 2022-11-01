from collections import Counter

fileName = ''
file = open('' + fileName, "r")

cnt = Counter(file)

lineNumber = 0
countDuplicateRows = 0

for key in cnt.keys():
    lineNumber += 1
    if cnt.get(key) > 1:
        countDuplicateRows += 1
        print('Found duplicate value at line number ' + str(lineNumber) + '. Line appears in file ' + str(
            cnt.get(key)) + ' times')
        print(key)

print('Completed File Processing.  ' + str(countDuplicateRows) + ' rows have duplicate values.')

file.close()


