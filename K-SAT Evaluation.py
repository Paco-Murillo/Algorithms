# A01374561 José Francisco Murillo Lozano
# A01376544 Mariana Paola Caballero Cabrera
# A01377744 Alejandro Torices Oliva


def obtenerParam(linea):
    linea = linea.split(" ")
    return int(linea[3])


def leerArchivo(filePath):
    file = open(filePath, 'r')
    linea = file.readline()
    variables = []
    while linea[0] != 'p':
        linea = file.readline()
    numClausulas = obtenerParam(linea)
    variableLine = file.readline()
    for index in range(len(variableLine) - 1):
        variables.append(bool(int(variableLine[index])))

    resultadoClausulas = []
    for index in range(numClausulas):
        linea = file.readline()
        linea = linea.split(" ")
        linea.pop()
        valores = []
        for indexStrToInt in range(len(linea)):
            valores.append(int(linea[indexStrToInt]))
        orForClausula = False
        for value in valores:
            if value < 0:
                orForClausula = orForClausula or not variables[abs(value)-1]
            else:
                orForClausula = orForClausula or variables[abs(value)-1]
        resultadoClausulas.append(orForClausula)

    return resultadoClausulas


def resultadoFinal(resultadoClausulas):
    resultadoFinal = True
    for clausula in resultadoClausulas:
        resultadoFinal = resultadoFinal and clausula
    return resultadoFinal


def main():
    resultadoClausulas = leerArchivo(input("Name of the file with problem conditions: "))
    print(resultadoFinal(resultadoClausulas))

main()