from re import A


def insertioSort(algaritimo):
    for step in range(1,len(algaritimo)):
        key = algaritimo[step]
        j = step -1
        while j>=0 and key < algaritimo[j]:
            algaritimo[j + 1] = algaritimo[j]
            j = j -1
            
        algaritimo[j+1]= key
data = [655, 89, 9, 5, 1, 7, 3, 11, 13, 15, 19, 21, 17, 29, 33, 23, 27, 39, 43, 37, 49, 77, 53, 153, 333, 59, 57, 245, 777, 111]
insertioSort(data)
print('algaritimo em ordem crescente') 
print(data)
