#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)


# convierte elementos de una lista tipo "34" a int
#                                        y  tipo "34.5" a float
def convertirElementosDeLista(lista):
    nueva_lista = []
    for elemento in lista:
        try:
            # Si es int
            nuevo_elemento = int(elemento)
        except ValueError:
            try:
                # Si es float
                nuevo_elemento = float(elemento)
            except ValueError:
                # Si es string
                nuevo_elemento = elemento
        nueva_lista.append(nuevo_elemento)
    return nueva_lista

l1 = input().split()
l2 = input().split()

t1 = tuple(convertirElementosDeLista(l1))
t2 = tuple(convertirElementosDeLista(l2))

salida = t2 + t1 + t2

print(salida)
