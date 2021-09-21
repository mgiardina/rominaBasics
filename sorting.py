import time

array = [10,-2,8,0,4,9,1,-1,-10,2]

def SelectionSort(array):
    start = time.time()

    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[j] < array[i]:
               array[j], array[i] = array[i], array[j]
    end = time.time()

    executionTime = end-start
    
    return array,executionTime

arraySort = SelectionSort(array)

print(f'Selection Sorted array: {arraySort[0]}')                
print(f'Selection sorting took: {arraySort[1]} seconds')

def BubbleSort(array):
    start = time.time()
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j] 
    end = time.time()
    executionTime = end-start

    return array,executionTime

arraySort = SelectionSort(array)

print(f'Bubble Sorted array:{arraySort[0]}')
print(f'Bubble sorting took: {arraySort[1]} seconds')

def InsertionSort(array):
    start = time.time()
    for i in range(1,len(array)):
    #    j = i
    #    while j> 0 and array[j-1] > array[j]:
    #        array[j] , array[j-1] = array[j-1] , array[j]
    #        j = j-1
    #    i = i+1
        if array[i-1] > array[i]:
            array[i] , array[i-1] = array[i-1] , array[i]
            
    end = time.time()
    executionTime = end-start
    return array,executionTime

arraySort = InsertionSort(array)

print(f'Insertion Sorted array:{arraySort[0]}')
print(f'Insertion sorting took: {arraySort[1]} seconds')