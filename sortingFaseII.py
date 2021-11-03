from randomarray import GenerateRandomArray
from nanoseconds import CurrentNanoSeconds

def MergeSort(array):
    if len(array) > 1:
        splitArray = len(array)//2  # divides the array

        L = array[:splitArray]
        R = array[splitArray:]
        MergeSort(L)
        MergeSort(R)
    
        indexL = indexR = indexM = 0 # index for right, index for left, index for merge
        while(indexL < len(L) and indexR < len(R)):
            if(L[indexL] <= R[indexR]):
                array[indexM] = L[indexL]
                indexL += 1
            else:
                array[indexM] = R[indexR]
                indexR += 1
            indexM += 1

        # if any elements are left either right or left

        while(indexL < len(L)):
            array[indexM] = L[indexL]
            indexL += 1
            indexM += 1

        while indexR < len(R):
            array[indexM] = R[indexR]
            indexR += 1
            indexM += 1 
    
def partition(array, low, indexPivot):
    index = low-1
    pivot = array[indexPivot]  #choose the pivot element
    for loop in range(low,indexPivot):
        if array[loop] <= pivot:  #element is less than pivot
                index += 1 
                (array[index] , array[loop]) = (array[loop] , array[index])

    array[index+1],array[indexPivot] = array[indexPivot] , array[index+1]    
    return(index+1)

def QuickSort(array, low, indexPivot): 
    # como tengo que partir derecha e izquierda del pivot
    # index+1 divide el array
    # ordenar desde el mas chico al pivot, y desde el pivot al mas grande

    if low < indexPivot:
        indexPartition = partition(array,low,indexPivot) # de aca obtengo el indice del pivot
        
        QuickSort(array,low,indexPartition-1)  # desde el inicio hasta el elemento que esta antes del pivot
        QuickSort(array,indexPartition+1,indexPivot) #desde el elemento que esta despues del pivot y el pivot

n= 10

arrayMerge = GenerateRandomArray(n)

#print(arrayMerge)

start = CurrentNanoSeconds()
MergeSort(arrayMerge)
end = CurrentNanoSeconds()
executionTimeMerge = end-start

arrayQuick = GenerateRandomArray(n)

#print(arrayQuick)

start = CurrentNanoSeconds()
QuickSort(arrayQuick,0,len(arrayQuick)-1)
end = CurrentNanoSeconds()
executionTimeQuick = end-start

print(f'Merge Sorted array: {arrayMerge}')                
print(f'Merge sorting took: {executionTimeMerge} seconds')

print(f'Quick Sorted array: {arrayQuick}')                
print(f'Quick sorting took: {executionTimeQuick} seconds')