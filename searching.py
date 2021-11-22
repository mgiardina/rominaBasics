from randomarray import GenerateRandomArray
from nanoseconds import CurrentNanoSeconds
from sorting import *
 

def linearSearch(array,value):
    for i in range(len(array)):
        print(array)
        if array[i] == value:
            indexSearch = i
            return indexSearch

def binarySearch(array,value):

    high = len(array)
    mid = high//2

    if high > 0:
        if array[mid] == value:
            return 'found'
        elif array[mid] < value:
                low = mid + 1
                array = array[low:high]
                return binarySearch(array,value)
        else:
            array = array[0:mid]
            return binarySearch(array,value)    
    else:
        return 'not found'

lenArray = 20
searchedElement = 41

#array = GenerateRandomArray(lenArray)
array = [41,25,84,62,2,7,12,4,37,62,41,33,72,96,145,-20,-7,0] #array for test

sortedArray = InsertionSort(array) # sort array for binary search

linearIndex = linearSearch(array,searchedElement)

print('Linear Search Algorithm')

if linearIndex == None:
    print(f'Value {searchedElement} is not in the array')
else:
    print(f'Value {searchedElement} is at {linearIndex} index')        

print('Binary Search Algorithm')

binary = binarySearch(sortedArray,searchedElement)

print(f'Value {searchedElement} is {binary}')
