# A01374561 José Francisco Murillo Lozano
# A01376544 Mariana Paola Caballero Cabrera
# A01377744 Alejadro Torices Oliva

def binarySearch(list, value):
    print(list)
    index = (len(list)-1)//2
    if len(list) == 0:
        return -1
    if list[index] > value:
        return binarySearch(list[:index], value)
    if list[index] < value:
        return binarySearch(list[index+1:], value)
    if list[index] == value:
        return index

def main():
    file = open("test_binary_search.txt", 'r')
    list = file.readline()
    list = list[1:len(list)-2]
    list = list.split(",")
    value = int(file.readline())
    file.close()
    for indexNumbers in range(len(list)):
        list[indexNumbers] = int(list[indexNumbers])
    print(len(list))
    print(list)
    print(binarySearch(list, value))

main()