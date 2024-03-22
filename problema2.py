#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)



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


t = convertirElementosDeLista(input().split())

t_inverso = tuple(t[::-1])

print(t_inverso)
