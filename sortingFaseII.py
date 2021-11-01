from randomarray import GenerateRandomArray
from nanoseconds import CurrentNanoSeconds

def MergeSort(array):
    if len(array) > 1:
        splitArray = len(array)//2  # divides the array

        L = array[:splitArray]
        R = array[splitArray:]
        MergeSort(L)
        MergeSort(R)
    
        indexL = indexR = indexM = 0 # index for right, index for left, index for merge
        while(indexL < len(L) and indexR < len(R)):
            if(L[indexL] < R[indexR]):
                array[indexM] = L[indexL]
                indexL += 1
            else:
                array[indexM] = R[indexR]
                indexR += 1
            indexM += 1

        # if any elements are left either right or left

        while(indexL < len(L)):
            array[indexM] = L[indexL]
            indexL += 1
            indexM += 1

        while indexR < len(R):
            array[indexM] = R[indexR]
            indexR += 1
            indexM += 1 
    
def quickSort(array, indexPivot):
    pivot = array[indexPivot]
    for index in range(len(array)-1):
        for loop in range(0,len(array)-1):
            if array(loop) < pivot:
                index += 1 
                array[loop] , array[index] = array[index] , array[loop] 
        
        array[index+1],pivot = pivot , array[index+1]    

# quickSort()
# Aca segun el video hay que hacer lo mismo desde 
# donde quedo el pivot, que sería index+1, hacia la derecha
# y a la izquierda, me confunden los indices
# no estoy segura si es quickSort desde 0 a index+1
# y quicksort desde index+1 hasta el final.  

n= 10

array = GenerateRandomArray(n)  
print(array)

MergeSort(array)
print(array)