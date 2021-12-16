from randomarray import GenerateRandomArray
from nanoseconds import CurrentNanoSeconds
from sorting import *
 

def linearSearch(array,searchedElement):
    for i in range(len(array)):
        if array[i] == searchedElement:
            indexSearch = i
            return indexSearch

def binarySearch(array,searchedElement, count = 1, index = 0):
    #print(array)
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

def binaryNonRecursive(array,searchedElement):
    low = 0
    high = len(array)

    while high > low:
        mid = (high+low)//2
        if array[mid] == searchedElement:
            return f'found at {mid}.'  
        elif array[mid] < searchedElement:
            low = mid + 1
        else:
            high = mid 
    return f'not found'           

def interpolationSearch(array,searchedElement):
    low = 0
    high = len(array) - 1
 
    while (low <= high and searchedElement >= array[low] and searchedElement <= array[high]):
        # low < high para recorrer todo el array
        # elemento es mayor al minimo valor que tiene el array
        # elemento es menor al máximo valor que tiene el array
        # esto es así porque esta ordenado
        
        index = low + ((searchedElement-sortedArray[low]) * (high - low)) // (sortedArray[high] - sortedArray[low])
        if array[index] == searchedElement:
            return f'found at {index}.'  
        elif array[index] < searchedElement:
            low = index + 1
        else:
            high = index   
    return f'not found'           

   

lenArray = 20
searchedElement = 140

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

print('Binary Non Recursive Algorithm')

binaryNonRec = binaryNonRecursive(sortedArray,searchedElement)

print(f'Value {searchedElement} is {binaryNonRec}')

print('Interpolation Search Algorithm')

interpolation = interpolationSearch(sortedArray,searchedElement)

print(f'Value {searchedElement} is {interpolation}')