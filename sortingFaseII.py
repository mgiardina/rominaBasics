from randomarray import GenerateRandomArray
from nanoseconds import CurrentNanoSeconds

## El merge divide en 2 partes el array hasta que queda un solo elemento (por
# eso el len(array)> 1 y parar la recursion). Va partiendo el array
# hasta que queda un elemento. Lo que no se es como unir despues
# la parte derecha y la izquierda, me quede en que queda un elemento
# y hay que empezar a unirlos

def MergeSort(array):
    if len(array) > 1:
        splitArray = len(array)//2

        L = array[:splitArray]
        R = array[splitArray:]
        MergeSort(L)
        MergeSort(R)

# En este creo que me maree y ya no supe donde hacer la recursion
# este lo base en el video que me habias pasado.        

def QuickSort(array):
    pivot = array[-1]
    for index in range(len(array)-1):
        for loop in range(0,len(array)-1):
            if array(loop) < pivot:
                index += 1 
                array[loop] , array[index] = array[index] , array[loop] 
        
        array[index+1],pivot = pivot , array[index+1]    

n= 10

array = GenerateRandomArray(n)  

MergeSort(array)