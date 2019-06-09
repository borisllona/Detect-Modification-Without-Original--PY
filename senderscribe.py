#!/usr/bin/env python3

import sys
import math
sys.setrecursionlimit(100000)
clau = '1101011'
SumX = []
SumY = []
inputfile = 0
outputfile = 0

def args():
    global inputfile,outputfile
    if len(sys.argv) > 2:
        inputfile = open(str(sys.argv[1]), "r")
        outputfile = open(str(sys.argv[2]), "w")
    else:
        outputfile = sys.stdout
        inputfile = sys.stdin

def xor(a, b):
    result = []

    # Actua com una porta logica xor 00->0,01->1,10->1,11->0
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)

def xor_recursiu(a, b):

    if len(a) == 0 or len(b) == 0:
        return ''

    if a[0] == b[0]:
        result = '0'
    else:
        result = '1'

    return result + xor_recursiu(a[1:], b[1:])



# Divisio en modul 2
def divisio(divident, divisor):
    # ajustem la llargada del residu per a tenir-ho com a referencia al dividir
    llarg = len(divisor)

    tmp = divident[0: llarg]

    while llarg < len(divident):

        if tmp[0] == '1':  # Entra si el bit de la esquerra es 1

            tmp = xor(divisor, tmp) + divident[llarg]

        else:  # Si el bit de l'esquerra es 0:

            # Si el bit de mes a l'esquerra es un 0, hem de dividir entre 0's
            tmp = xor('0' * llarg, tmp) + divident[llarg]

        llarg += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * llarg, tmp)

    residu = tmp
    return residu

def divisio_recursiva(divident, divisor,llarg="",temp=""):
    # ajustem la llargada del residu per a tenir-ho com a referencia al dividir
    if not llarg: llarg = len(divisor)
    if not temp: temp = divident[0: llarg]

    if llarg < len(divident):
        if  temp[0] == '1':
            temp = xor_recursiu(divisor, temp) + divident[llarg]
        else:
            temp = xor_recursiu('0'*llarg, temp) + divident[llarg]

        llarg += 1

        divisio_recursiva(divident,divisor,llarg,temp)
    else:
        if temp[0] == '1':
            return xor_recursiu(divisor, temp)
        else:
            return xor_recursiu('0'*llarg, temp)

    return divisio_recursiva(divident, divisor, llarg, temp)


def ajustarDades(data, clau):
    l_clau = len(clau)

    # Afegim n-1 0's al final de el nombre binary equivalent al nostre text original.
    afegir0 = data + '0' * (l_clau - 1)
    residu = divisio(afegir0, clau)

    # Afegim la parula inicial amb el residu de la divisio entre la clau.
    paraula = data + residu
    return residu

def ajustarDades_resursiu(data, clau):
    l_clau = len(clau)

    # Afegim n-1 0's al final de el nombre binary equivalent al nostre text original.
    afegir0 = data + '0' * (l_clau - 1)
    residu = divisio(afegir0, clau)

    # Afegim la parula inicial amb el residu de la divisio entre la clau.
    paraula = data + residu
    return residu


def plumbusToBinary():
    binary = ''

    byte = inputfile.read(1)
    while byte:
        outputfile.write(byte)
        if byte == '0' or byte == '1':
            binary = binary + str(byte)
        else:
            binary = binary + str(bin(ord(byte))[2:])
        byte = inputfile.read(1)

    return binary

def plumbusToBinary_resursiu():
    binary = ''

    byte = inputfile.read(1)
    if not byte: return binary
    outputfile.write(byte)
    if byte == '0' or byte == '1':
        binary = binary + str(byte)
    else:
        binary = binary + str(bin(ord(byte))[2:])

    return binary + plumbusToBinary_resursiu()

def createMatrix():
    global SumX, SumY
    digits = []

    inputfile = open("original.txt", "r")

    byte = inputfile.read(1)
    while byte:
        digits.append(byte)
        byte = inputfile.read(1)

    x = int(math.ceil(math.sqrt(len(digits))))  # Arrel cuadrada de la longitud de la llista i la aproximem a la alta
    y = int(math.ceil(math.sqrt(len(digits))))

    matrix = [[0 for i in range(x)] for j in range(y)]  # Creo la matriu amb les dimensions de els elements llegits
    for i in range(0, x):
        for j in range(0, y):
            if not digits:
                matrix[i][j] = ''
            else:
                matrix[i][j] = digits[0]
                digits.pop(0)
        print(matrix[i])

    for i in range(0, x):
        sumx = 0
        sumy = 0
        for j in range(0, y):
            if matrix[i][j] != '' and matrix[j][i] != '':
                sumx += ord(str(matrix[i][j]))
                sumy += ord(str(matrix[j][i]))
        if sumx != 0 and sumy != 0:
            SumX.append(sumx)
            SumY.append(sumy)
    # Ficar al sender i enviar informacio abans de la clau.

    return SumX, SumY


def writeSums(X, Y):
    while X:
        outputfile.write(str(X[0]))
        X = X[1:]
    while Y:
        outputfile.write(str(Y[0]))
        Y = Y[1:]

def writeSums_resursiu(X, Y):
    if not X: return 0
    outputfile.write(str(X[0]))
    if not Y: return 0
    outputfile.write(str(Y[0]))

    return writeSums_resursiu(X[1:],Y[1:])

def iterative():
    data = plumbusToBinary()
    dividentIResidu = ajustarDades(data, clau)
    outputfile.write(dividentIResidu)

def recursive():
    data = plumbusToBinary_resursiu()
    dividentIResidu = ajustarDades_resursiu(data, clau)
    outputfile.write(dividentIResidu)

def findandcorrect():
    SumX, SumY = createMatrix()
    #writeSums_resursiu(SumX,SumY)
    writeSums(SumX, SumY)

if __name__ == "__main__":
    args()
    iterative()
    #recursive()
    #findandcorrect()
