# potential enhancement: update code to output line number of special characters found in file

sourceFilePath = ''
sourceFileName = ''
sourceFile = open(sourceFileName + sourceFilePath)

r = sourceFile.read()

status = "No special characters found"

for line in r:
    for char in line:
        if (ord(char) < 32 or ord(char) > 126) and ord(char) != 10 and ord(char) != 0:
            print("Special character " + str(ord(char)) + " found on line number ")
            status = "Special characters found"


print("Status: " + status)

