from randomarray import GenerateRandomArray
from nanoseconds import CurrentNanoSeconds
 

def linearSearch(array,value):
    for i in range(len(array)):
        if array[i] == value:
            indexSearch = i
        else:
            indexSearch = None
    return indexSearch

n = 20

array = GenerateRandomArray(n)

linearIndex = linearSearch(array,5)

if linearIndex ==None:
    print(f'Value is not in the array')
else:
    print(f'Value is at {linearIndex} index')        