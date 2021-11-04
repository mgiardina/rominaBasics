from randomarray import GenerateRandomArray
from nanoseconds import CurrentNanoSeconds


def SelectionSort(array):
    for i in range(len(array)-1):
        minimun = i
        
        for j in range(i+1,len(array)):
            if array[j] < array[minimun]:
                minimun =j
        
        array[minimun], array[i] = array[i], array[minimun]
    return array

def BubbleSort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j] 
    return array

def InsertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j>= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1]=key
    return array


def MergeSort(array):
    if len(array) > 1:
        splitArray = len(array)//2  

        L = array[:splitArray]
        R = array[splitArray:]
        MergeSort(L)
        MergeSort(R)
    
        indexL = indexR = indexM = 0 
        while(indexL < len(L) and indexR < len(R)):
            if(L[indexL] <= R[indexR]):
                array[indexM] = L[indexL]
                indexL += 1
            else:
                array[indexM] = R[indexR]
                indexR += 1
            indexM += 1

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
    pivot = array[indexPivot]  
    for loop in range(low,indexPivot):
        if array[loop] <= pivot:  
                index += 1 
                (array[index] , array[loop]) = (array[loop] , array[index])

    array[index+1],array[indexPivot] = array[indexPivot] , array[index+1]    
    return(index+1)

def QuickSort(array, low, indexPivot): 
    if low < indexPivot:
        indexPartition = partition(array,low,indexPivot) 
        
        QuickSort(array,low,indexPartition-1)  
        QuickSort(array,indexPartition+1,indexPivot) 

##

n= 10000

array = GenerateRandomArray(n)

start = CurrentNanoSeconds()
arraySelectSort = SelectionSort(array)
end = CurrentNanoSeconds()
executionTimeSelec = end-start

start = CurrentNanoSeconds()
arrayBubbleSort = BubbleSort(array)
end = CurrentNanoSeconds()
executionTimeBubb = end-start

start = CurrentNanoSeconds()
arrayInsertionSort = InsertionSort(array)
end = CurrentNanoSeconds()
executionTimeInser = end-start

arrayMerge = GenerateRandomArray(n)

start = CurrentNanoSeconds()
MergeSort(arrayMerge)
end = CurrentNanoSeconds()
executionTimeMerge = end-start

arrayQuick = GenerateRandomArray(n)

start = CurrentNanoSeconds()
QuickSort(arrayQuick,0,len(arrayQuick)-1)
end = CurrentNanoSeconds()
executionTimeQuick = end-start

#print(f'Selection Sorted array: {arraySelectSort}')                
print(f'Selection sorting took: {executionTimeSelec} seconds')

#print(f'Bubble Sorted array:{arrayBubbleSort}')
print(f'Bubble sorting took: {executionTimeBubb} seconds')

#print(f'Insertion Sorted array:{arrayInsertionSort}')
print(f'Insertion sorting took: {executionTimeInser} seconds')

#print(f'Merge Sorted array: {arrayMerge}')                
print(f'Merge sorting took: {executionTimeMerge} seconds')

#print(f'Quick Sorted array: {arrayQuick}')                
print(f'Quick sorting took: {executionTimeQuick} seconds')