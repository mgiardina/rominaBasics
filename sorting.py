import time
import numpy as np

## Functions

def GenerateRandomArray(l,h,n):
    array= np.random.randint(l,h,n)
    return array

def CurrentNanoSeconds():
    return round(time.time() * 10000000000)

def SelectionSort(array):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[j] < array[i]:
               array[j], array[i] = array[i], array[j]
    return array

def BubbleSort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j] 
    return array

def InsertionSort(array):
    for i in range(1,len(array)):
    #    j = i
    #    while j> 0 and array[j-1] > array[j]:
    #        array[j] , array[j-1] = array[j-1] , array[j]
    #        j = j-1
    #    i = i+1
        if array[i-1] > array[i]:
            array[i] , array[i-1] = array[i-1] , array[i]
    return array

##

l= -1500
h= 1500
n= 1000

array = GenerateRandomArray(l,h,n)

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