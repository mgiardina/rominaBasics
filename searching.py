from randomarray import GenerateRandomArray
from nanoseconds import CurrentNanoSeconds
from sorting import *
 

def linearSearch(array,searchedElement):
    for i in range(len(array)):
        if array[i] == searchedElement:
            indexSearch = i
            return indexSearch

def binarySearch(array,searchedElement, count = 1, index = 0):
    print(array)
    high = len(array)
    mid = high//2
    #print('comienzo',array[mid],mid) ##test
    if high > 0:
        if array[mid] == searchedElement:
            index = index + mid 
            return f'found at {index}. Function was called {count} times'
        elif array[mid] < searchedElement:
            low = mid + 1
            array = array[low:high]
            index = index + mid + 1
            #print('mayor',mid,index) ##test
            return  binarySearch(array,searchedElement,count + 1, index)
        else:
            index = 0 
            #print('menor',index) ##test
            array = array[0:mid]
            
            return binarySearch(array,searchedElement,count + 1,index)   
    else:
        return f'not found. Function was called {count} times'


lenArray = 20
searchedElement = 7

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
