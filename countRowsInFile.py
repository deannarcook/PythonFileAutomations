import pandas as pd

#  provide path of source file. use \\ in path.
sourceFilePath = ''
# provide name of source file with file extension
sourceFileName = ''
sourceFile = pd.read_csv(sourceFilePath + sourceFileName)

print(sourceFileName + ' has ' + str(len(sourceFile)) + ' rows')