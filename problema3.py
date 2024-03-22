#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]

def arbolTrinario(numero):
    return [numero, [], [], []]

def insertaEnArbolTrinario(arbol, numero):
    if arbol == []:
        arbol += arbolTrinario(numero)
    elif numero > arbol[0]:
        insertaEnArbolTrinario(arbol[3], numero)
    elif numero < arbol[0]:
        insertaEnArbolTrinario(arbol[1], numero)
    else:
        insertaEnArbolTrinario(arbol[2], numero)
        


def crearArbolTrinario(lista):
    arbol = []
    for elemento in lista:
        insertaEnArbolTrinario(arbol, elemento)
    return arbol


t = input().split()
nums = [int(n) for n in t]

arbol = crearArbolTrinario(nums)

print(arbol)
