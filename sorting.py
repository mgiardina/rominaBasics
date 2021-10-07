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
        while j> 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1]=key
    return array

##

n= 1000

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

print(f'Selection Sorted array: {arraySelectSort}')                
print(f'Selection sorting took: {executionTimeSelec} seconds')

print(f'Bubble Sorted array:{arrayBubbleSort}')
print(f'Bubble sorting took: {executionTimeBubb} seconds')

print(f'Insertion Sorted array:{arrayInsertionSort}')
print(f'Insertion sorting took: {executionTimeInser} seconds')