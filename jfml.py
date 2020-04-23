# A01374561 José Francisco Murillo Lozano
# A01376544 Mariana Paola Caballero Cabrera
# A01377744 Alejadro Torices Oliva

def bucketSort(list):
    pass


def insertionSort(list):
    pass


def bubbleSort(list):
    pass


def quickSort(list):
    pass


def radixSort(list):
    return list


def mergeSort(list):
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
            print(quickSort(list))
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