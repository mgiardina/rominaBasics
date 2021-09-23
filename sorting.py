import time

array = [10,-2,8,0,4,9,1,-1,-10,2,15,8,3,-7,25,37,-25,5,11,0]

## Functions

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

start = time.time()
arraySelectSort = SelectionSort(array)
end = time.time()
executionTimeSelec = end-start
executionTimeSelec = CurrentNanoSeconds()

start = time.time()
arrayBubbleSort = BubbleSort(array)
end = time.time()
executionTimeBubb = end-start
executionTimeBubb = CurrentNanoSeconds()

start = time.time()
arrayInsertionSort = InsertionSort(array)
end = time.time()
executionTimeInser = end-start
executionTimeInser = CurrentNanoSeconds()

print(f'Selection Sorted array: {arraySelectSort}')                
print(f'Selection sorting took: {executionTimeSelec} seconds')

print(f'Bubble Sorted array:{arrayBubbleSort}')
print(f'Bubble sorting took: {executionTimeBubb} seconds')

print(f'Insertion Sorted array:{arrayInsertionSort}')
print(f'Insertion sorting took: {executionTimeInser} seconds')