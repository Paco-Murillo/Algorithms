k = 3
m = 91
var = 20
x = []



def readFile(fileName):
    file = open(fileName, "r")
    strList = ""
    file.readline()
    line = file.readline()
    variableLine = file.readline()
    for i in range(len(variableLine)-1):
        x.append(int(variableLine[i]))

    while line != "":
        strList += line
        line = file.readline()
    strList = strList.split(",")
    file.close()
    print(x)

readFile("Instance_3SAT_example.txt")
