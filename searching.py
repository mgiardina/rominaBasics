from randomarray import GenerateRandomArray
from nanoseconds import CurrentNanoSeconds
from sorting import *
 

def linearSearch(array, searchedElement):
    for i in range(len(array)):
        if array[i] == searchedElement:
            indexSearch = i
            return indexSearch

def binarySearch(array, searchedElement, index, high, count = 1):
    if high >= index:
        mid = index + (high - index) // 2
        if array[mid] == searchedElement:
            return f'found at {mid}. Function was called {count} times'
        elif array[mid] < searchedElement:
            newMid = mid + 1
            return binarySearch(array, searchedElement, newMid, high, count + 1)
        else:
            newMid = mid - 1
            return binarySearch(array, searchedElement, index, newMid, count + 1)
    else:
        return f'not found. Function was called {count} times'

def binaryNonRecursive(array, searchedElement, low, high):

    while high > low:
        mid = (high + low) // 2
        if array[mid] == searchedElement:
            return f'found at {mid}.'  
        elif array[mid] < searchedElement:
            low = mid + 1
        else:
            high = mid 
    return f'not found' 

def interpolationSearch(array, searchedElement, low, high, count = 1):
    
    if high >= low and searchedElement >= array[low] and searchedElement <= array[high]:
        index = low + ((searchedElement - array[low]) * (high - low)) // (array[high] - array[low])

        if array[index] == searchedElement:
            return f'found at {index}. Function was called {count} times'
        elif array[index] < searchedElement:
            newIndex = index + 1
            return interpolationSearch(array, searchedElement, newIndex, high, count + 1)
        else:
            newIndex = index
            return interpolationSearch(array, searchedElement, index, newIndex, count + 1)
    else:
        return f'not found. Function was called {count} times'    


def interpolationNonRecursive(array, searchedElement):
    low = 0
    high = len(array) - 1
 
    while (high >= low and searchedElement >= array[low] and searchedElement <= array[high]):
        # low < high para recorrer todo el array
        # elemento es mayor al minimo valor que tiene el array
        # elemento es menor al máximo valor que tiene el array
        # esto es así porque esta ordenado
        
        # Formula derivada de la ecuación de una recta para 
        # encontrar el elemento más próximo al elemento que quiero buscar

        index = low + ((searchedElement - array[low]) * (high - low)) // (array[high] - array[low])
        
        # Si el elemento a buscar esta en el lugar del index, me quedo con ese valor  
        if array[index] == searchedElement:
            return f'found at {index}.'  
        elif array[index] < searchedElement:
            # si el elemento que busco es mayor al elemento que esta en la ubicacion que obtengo 
            # en la ecuación, empieza a buscar nuevamente por la parte derecha del array, por eso
            # el comienzo del array estará desde el index + 1
            low = index + 1
        else:
            # si el elemento que busco es menor al elemento que esta en la ubicacion que obtengo 
            # en la ecuación, empieza a buscar nuevamente por la parte izquierda del array, por eso
            # el comienzo del array sigue en el lugar inicial y el fin de array es en la posición del 
            # index
            high = index   
    return f'not found'           

   

lenArray = 20
searchedElement = 72

#array = GenerateRandomArray(lenArray)
array = [41,25,84,62,2,7,12,4,37,62,41,33,72,96,145,-20,-7,0] #array for test

n = len(array)

sortedArray = InsertionSort(array) # sort array for binary search

print(sortedArray)

linearIndex = linearSearch(array, searchedElement)

print('Linear Search Algorithm')

if linearIndex == None:
    print(f'Value {searchedElement} is not in the array')
else:
    print(f'Value {searchedElement} is at {linearIndex} index')        

print('Binary Search Algorithm')

binary = binarySearch(sortedArray, searchedElement, 0, n)

print(f'Value {searchedElement} is {binary}')

print('Binary Non Recursive Algorithm')

binaryNonRec = binaryNonRecursive(sortedArray, searchedElement, 0, n)

print(f'Value {searchedElement} is {binaryNonRec}')

print('Interpolation Search Algorithm')

interpolation = interpolationSearch(sortedArray, searchedElement, 0, n-1)

print(f'Value {searchedElement} is {interpolation}')

print('Interpolation Non Recursive Algorithm')

interpolationNonRec = interpolationNonRecursive(sortedArray, searchedElement)

print(f'Value {searchedElement} is {interpolationNonRec}')