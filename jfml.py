# A01374561 José Francisco Murillo Lozano
# A01376544 Mariana Paola Caballero Cabrera
# A01377744 Alejadro Torices Oliva


import math


def bucketSort(list):
    biggest = 0

    for number in list:
        if number > biggest:
            biggest = number

    buckets = [[0, 0]] * (biggest+1)

    for number in list:
        if buckets[number][0] != number or number == 0:
            buckets.insert(number, [number, 0])
            buckets.pop(number+1)
        buckets[number][1] += 1
        print(buckets)

    new_list = []

    for index in range(len(buckets)):
        count = buckets[index][1]
        if count == 0:
            continue
        number = buckets[index][0]
        for times in range(count):
            new_list.append(number)

    return new_list




def insertionSort(list):
    for index in range(1, len(list)):
        value = list[index]
        for indexSort in range(index):
            if value < list[indexSort]:
                print(list)
                list.pop(index)
                list.insert(indexSort, value)
                break
    return list



def bubbleSort(list):
    for i in range(1, len(list)):
        for j in range(0, len(list) - i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
            print(list)


def divide(list, first, last):
    i = j = first
    print(list)

    while j < last:
        if list[j] <= list[last]:
            list[i], list[j] = list[j], list[i]
            i += 1
        j += 1
    list[i], list[last] = list[last], list[i]
    return i


def quickSort(list, first, last):
    if first < last:
        index = divide(list, first, last)
        quickSort(list, first, index-1)
        quickSort(list, index+1, last)


def countingSort(list, position):
    size = len(list)
    count = [0] * 10

    for index in range(0, size):
        countIndex = list[index] // position
        count[countIndex % 10] += 1

    for index in range(1, 10):
        count[index] += count[index - 1]

    output = [0] * size

    for index in range(size-1, -1, -1):
        countIndex = list[index] // position
        output[count[countIndex % 10] - 1] = list[index]
        count[countIndex % 10] -= 1

    for index in range(0, size):
        list[index] = output[index]

    print(list)


def radixSort(list):
    biggestElement = max(list)

    for index in range(len(str(biggestElement))):
        position = 10**index
        countingSort(list, position)


def mergeSort(list):
    if len(list) == 1:
        return

    midpoint = len(list) // 2
    leftSide = list[:midpoint]
    rightSide = list[midpoint:]

    mergeSort(leftSide)
    mergeSort(rightSide)

    leftIndex = 0
    rightIndex = 0
    mainIndex = 0

    while leftIndex < len(leftSide) and rightIndex < len(rightSide):
        if leftSide[leftIndex] <= rightSide[rightIndex]:
            list[mainIndex] = leftSide[leftIndex]
            leftIndex += 1
        else:
            list[mainIndex] = rightSide[rightIndex]
            rightIndex += 1
        mainIndex += 1

    for index in range(leftIndex, len(leftSide)):
        list[mainIndex] = leftSide[index]
        mainIndex += 1

    for index in range(rightIndex, len(rightSide)):
        list[mainIndex] = rightSide[index]
        mainIndex += 1

    print(list)
    return list


def menu():
    print("************************************\n          Algorithm Menu\n************************************")
    print("%2d. BucketSort    Algorithm" % 1)
    print("%2d. InsertionSort Algorithm" % 2)
    print("%2d. BubbleSort    Algorithm" % 3)
    print("%2d. QuickSort     Algorithm" % 4)
    print("%2d. RadixSort     Algorithm" % 5)
    print("%2d. MergeSort     Algorithm\n" % 6)
    print("Enter 0 or less to exit.\n")
    return int(input("Select one of the above algorithms to run.\nEnter its number: "))


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


def main():
    list = readCSV("numbers.txt")
    election = menu()
    while election > 0:  # election <= 0
        if election == 1:
            print(bucketSort(list))
        elif election == 2:
            print(insertionSort(list))
        elif election == 3:
            print(bubbleSort(list))
        elif election == 4:
            quickSort(list, 0, len(list)-1)
        elif election == 5:
            print(radixSort(list))
        elif election == 6:
            print(mergeSort(list))
        else:
            print("Ingresa una opcion correcta")
        if bool(int(input("Do you want to run the menu again? '1' or '0'\n"))):
            election = menu()
        else:
            return election

main()
