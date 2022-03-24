# -*- coding: utf-8 -*-
"""ordernamiento.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YJ92lzCLPYvfXx1iiCNBVNxpb9J-tWGI
"""

#Ordenamiento en burbuja

lista = [50,30,32,15,60,58,22,21,3,1,0,14,18,5,7,9,24,80,79,67,54,13]
print(len(lista))

def metodoBurbuja(lista):
  # Calcular la longitud de la lista
  longitud = len(lista)
  # Recorrer la lista por longitud
  for el in range(longitud):
    # Recorremos el ciclo pero ahora hasta el penultimo elemento
    for indice_actual in range(longitud -1):
      # se obtiene el indice siguiente
      index_sig = indice_actual + 1
      # Si el index actual es mayor que el index siguiente
      if lista[indice_actual] > lista[index_sig]:
        # Intercambiar elementos con una asignación de concatenamiento
        lista[index_sig], lista[indice_actual] = lista[indice_actual], lista[index_sig]


print('Original: ')
print(lista)
metodoBurbuja(lista)
print('Ordenado: ')
print(lista)

# Insert Sort
lista = [50,30,32,15,60,58,22,21,3,1,0,14,18,5,7,9,24,80,79,67,54,13]

def InsertSort(lista):
  # Obtener la logitud de la lista
  # Dar por hecho que la posición 0 es la predeterminada
  longitud = len(lista)
  # recorrer la lista para obtener valores a insertar
  for el in range(1, longitud):
    # Almacenar en una variable el elemento a insertar
    item_insert = lista[el]
    # Obtener index del elemento anterior
    index_ant = el - 1
    # Guardar el elemento anterior
    # item_anterior = lista[index_ant] 80

    # con while, mover todos los elementos de la lista hacia la derecha si es mayor que
    # con while, mover todos los elementos de la lista hacia la izquierda si es menor que
    while index_ant >= 0 and lista[index_ant] < item_insert:
      # mientras el item anterior sea mayor se recorrera el while
      lista[index_ant + 1] = lista[index_ant]
      # restamos a elemento el index para que siempre regrese a seleccionar el anterior
      index_ant -= 1
    # Hacer del elemento que se comparó
    lista[index_ant + 1] = item_insert
print('Original: ')
print(lista)
InsertSort(lista)
print('Ordenado: ')
print(lista)

# Quick Sort
lista = [50,30,32,15,60,58,22,21,3,1,0,14,18,5,7,9,24,80,79,67,54,13]
def QuickSort(lista):
  # Elegir un elemento
  # Declarar posiciones 
  izquierda = []
  centro  = []
  derecha = []

  # Obtener la longitud de la lista
  longitud = len(lista)

  # Sí la longitud es mayor que 1
  if longitud > 1:
    # Se selecciona el index para que sea pivote
    pivote = lista[0]
    # Recorrer la lista
    for elemento in lista:
      # Si elemento es menor que el pivote
      if elemento < pivote:
        izquierda.append(elemento)
      # Si el elemento es igual al pivote
      elif elemento == pivote:
        centro.append(elemento)
      # Si el elemento es mayor que el pivote
      elif elemento > pivote:
        derecha.append(elemento)
    print(izquierda + ["-"] + centro + ["-"] + derecha)
    # regresar la función quicksort pero ahora con izquierda y derecha
    return QuickSort(izquierda) + centro + QuickSort(derecha)
  else:
    return lista
print(lista)
print(QuickSort(lista))