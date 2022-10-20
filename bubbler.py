import random
def bubbleSort(lista):
    for p in range(len(lista)-1,0,-1):
        for i in range(p):
            if lista[i]>lista[i+1]:
                resultado = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = resultado

lista = []
for i in range(0,10,1):
    lista.append(random.randint(1,100))
bubbleSort(lista)
print(lista)