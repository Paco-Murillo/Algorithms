# A01374561 José Francisco Murillo Lozano
# A01376544 Mariana Paola Caballero Cabrera
# A01377744 Alejandro Torices Oliva
import random
import requests
import random


def txtToBoolList(text):
    boolList = []
    try:
        for value in range(int(text)):
            boolList.append(True if random.randint(0, 1) else False)
    except ValueError:
        text = text.split("\n")
        for value in text:
            if value != '':
                boolList.append(True if int(value) == 1 else False)

    return list(boolList)


def obtenerRandBool(num=1):
    respuesta = requests.get(
        "http://www.random.org/integers/?num=" + str(num) + "&min=0&max=1&col=1&base=10&format=plain&rnd=new")
    if respuesta.ok:
        if num > 1:
            return txtToBoolList(respuesta.text)
        else:
            return bool(respuesta.text)
    else:
        if num > 1:
            return txtToBoolList(num)
        else:
            return bool(random.randint(0, 1))


def obtenerParam(linea):
    linea = linea.split(" ")
    return int(linea[2]), int(linea[3])


def leerArchivo(filePath):
    file = open(filePath, 'r')
    linea = file.readline()
    while linea[0] != 'p':
        linea = file.readline()
    numVariables, numClausulas = obtenerParam(linea)
    file.readline()
    valClausulas = []
    for index in range(numClausulas):
        linea = file.readline()
        linea = linea.split(" ")
        linea.pop()

        valores = []
        for indexStrToInt in range(len(linea)):
            valores.append(int(linea[indexStrToInt]))
        valClausulas.append(list(valores))

    return valClausulas, numVariables


def evaluarKSAT(clausula, variables):
    resultadoClausula = False
    for value in clausula:
        if value < 0:
            resultadoClausula = resultadoClausula or not variables[abs(value) - 1]
        else:
            resultadoClausula = resultadoClausula or variables[abs(value) - 1]
    return resultadoClausula


def cambiarValor(valsClausula, variables, tipodeKSAT):
    for index in range(tipodeKSAT):
        if obtenerRandBool() or index == tipodeKSAT - 1:
            valor = valsClausula[index]
            if valor < 0:
                variables[abs(valor) - 1] = False
            else:
                variables[abs(valor) - 1] = True
            break


def schoningKSAT(valClausulas, numVariables):
    tipoDeKSAT = len(valClausulas[0])
    variables = obtenerRandBool(numVariables)
    termina = 3 * numVariables
    while termina > 0:
        for indexClausula in range(len(valClausulas)):
            if not evaluarKSAT(valClausulas[indexClausula], variables):
                cambiarValor(valClausulas[indexClausula], variables, tipoDeKSAT)
                break
            if indexClausula == len(valClausulas) - 1:
                return variables
        termina -= 1
    return termina


def main():
    valClausulas, numVariables =leerArchivo(input("Name of the file with problem conditions: "))
    res = schoningKSAT(valClausulas, numVariables)
    print(res if res != 0 else "Se corrio 3n veces y no se llego a la solucion")

main()
