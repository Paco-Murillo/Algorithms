# A01374561 José Francisco Murillo Lozano
# A01376544 Mariana Paola Caballero Cabrera
# A01377744 Alejandro Torices Oliva

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getValue(self):
        return self.value



def readCSV(fileName):
    file = open(fileName, "r")
    strList = ""
    line = file.readline()
    while line != "":
        strList += line
        line = file.readline()
    strList = strList.split(",")
    file.close()

    for index in range(len(strList)):
        strList[index] = int(strList[index])

    return strList


def binaryTreeGen(list):
    binaryTree = [[0, 0]]


def main():
    list = readCSV("prueba.txt")
    treeList = binaryTreeGen(list)

main()