import time


def insertionSort(list):
    for index in range(1, len(list)):
        value = list[index]
        for indexSort in range(index):
            if value < list[indexSort]:
                list.pop(index)
                list.insert(indexSort, value)
                break
    return list


def divide(list, first, last):
    i = j = first
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
    print(list)


def readCSV(fileName):
    file = open(fileName, "r")
    strList = ""
    line = file.readline()
    while line != "":
        strList += line
        line = file.readline()
    list = strList.split(",")
    file.close()

    for index in range(len(list)):
        list[index] = int(list[index])

    return list


def menu():
    print("************************************\n          Algorithm Menu\n************************************")
    print("%2d. InsertionSort Algorithm" % 1)
    print("%2d. QuickSort     Algorithm" % 2)
    print("Enter any number different from the above to exit.\n")
    return int(input("Select one of the above algorithms to run.\nEnter its number: "))


def main():
    election = menu()
    while 3 > election > 0:
        list = readCSV(input("Insert the name of the text file with the input (with extension): "))
        if election == 1:
            startTime = time.time()
            print("\n\n%s\nExecuted in %s seconds \n\n" % (insertionSort(list), (time.time()-startTime)))
        if election == 2:
            startTime = time.time()
            print("\n\n%s\nExecuted in %s seconds \n\n" % (quickSort(list, 0, len(list)), (time.time() - startTime)))
        election = menu()

main()