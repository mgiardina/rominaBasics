import random

def GenerateRandomArray(n):
    array = [random.randint(-500,500) for i in range(n)]
    return array    

def linearSearch(array,value):
    for i in range(len(array)):
        if array[i] == value:
            indexSearch = i
        else:
            indexSearch = None
    return indexSearch

array = GenerateRandomArray(20)

linearIndex = linearSearch(array,5)

if linearIndex ==None:
    print(f'Value is not in the array')
else:
    print(f'Value is at {linearIndex} index')        