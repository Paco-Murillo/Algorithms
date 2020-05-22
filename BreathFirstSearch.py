# A01374561 José Francisco Murillo Lozano
# A01376544 Mariana Paola Caballero Cabrera
# A01377744 Alejandro Torices Oliva


def readConnections(filePath):
    file = open(filePath, "r", encoding="UTF-8")
    line = file.readline()
    split = line.split(",")
    matrix = []
    maxValue = 0
    for char in line:
        try:
            maxValue = int(char) if int(char) > maxValue else maxValue
        except ValueError:
            continue
    for index in range(maxValue+1):
        matrix.append(list())
    for index in range(0, len(split) - 1, 2):
        for char1 in split[index]:
            if char1 != "(":
                char1 = int(char1)
                for char2 in split[index + 1]:
                    if char2 != ")":
                        char2 = int(char2)
                        matrix[char1].insert(0, char2)
                        matrix[char2].insert(0, char1)
    return matrix, maxValue


def breathFirstSearch(matrix, num, queue, stack, maxValue, init):
    if num not in stack and matrix[num] != []:
        stack.append(num)
    print("\nStack: " + str(stack))
    for neighbor in matrix[num]:
        if neighbor not in stack and neighbor not in queue:
            queue.insert(0, neighbor)

    print("Queue: " + str(queue))

    if len(stack) == maxValue:
        raise SystemExit("Ran smoothly through the entire graph")

    try:
        neighbor = queue.pop()
        breathFirstSearch(matrix, neighbor, queue, stack, maxValue, init)
    except IndexError:
        raise SystemExit("Graph not entirely connected")


def main():
    matrix, maxValue = readConnections(input("Name of the file with graph details: "))
    while True:
        try:
            print("Enter a negative number to close. ")
            num = int(input("Enter number of node to start in: "))
            break
        except ValueError:
            print("Enter a correct value.")
    while num >= 0:
        try:
            stack = []
            breathFirstSearch(matrix, num, [num], stack, maxValue, num)
        except SystemExit as e:
            print(e)
            break
    print("\n\n*********** Final ***********\n")
    print("Matrix of unions: " + str(matrix))
    print("Final stack: " + str(stack))


main()
