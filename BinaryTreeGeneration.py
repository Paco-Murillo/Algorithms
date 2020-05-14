# A01374561 José Francisco Murillo Lozano
# A01376544 Mariana Paola Caballero Cabrera
# A01377744 Alejandro Torices Oliva

tree = []

class Node:
    right = None
    left = None

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

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
    for char in line:
        if char in "{}":
            line = line.replace(char, "")
    while line != "":

        strList += line
        line = file.readline()


    strList = strList.split(",")
    file.close()

    for index in range(len(strList)):
        strList[index] = int(strList[index])

    return strList


def insertNode(node, value):
    if node.value > value:
        if node.left is None:
            node.left = Node(value)
        else:
            insertNode(node.left, value)
    else:
        if node.right is None:
            node.right = Node(value)
        else:
            insertNode(node.right, value)


def binaryTreeGen(list):
    node = Node(list[0])
    for index in range(1, len(list)):
        insertNode(node, list[index])
    return node


def printTree(node, level):
    if level is 0:
        tree.append(node.value)
    children = []

    if node.left is not None:
        children.append(node.left.value)
    else:
        children.append(" ")
    if node.right is not None:
        children.append(node.right.value)
    else:
        children.append(" ")
    level = level + 1
    tree.append([])
    if tree[level] is not None:
        tree[level].append(children)
    else:
        tree[level] = children
    if node.left is not None:
        printTree(node.left, level)
    if node.right is not None:
        printTree(node.right, level)



def main():
    print("\n Aesthetic binary tree:")
    list = readCSV("prueba.txt")
    root = binaryTreeGen(list)
    printTree(root, 0)
    for n in tree:
       print(str(n).center(150))


main()
