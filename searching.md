# Searching algorithms 

## Linear searching
Linear search algorithm is the simplest one. Sequentially read each element one by one on a given array until desired element is found. This method may be not effective for arrays with large number of items.

<img src="https://www.tutorialspoint.com/data_structures_algorithms/images/linear_search.gif" width="300" height="100"/>

## Binary searching
Binary search needs a sorted array to start the process. So, if the elements are not sorted, the array must be sorted for the implementation. This algorithm can be implemented with an iterative method or a recursive method.
This method search the middle element of an array and it compares this value with the value being searched. If searched value is in the middle, then this position is return. Else, if the searched value is greater than the middle one, the process is made within the upper half. Otherwise, the lower half is used. This process is made until the searched element is found. 

## Interpolation searching  
This algorithm is an improvement of the Binary search. The array must be sorted and equally distributed first. The interpolation search starts the searching from the element closest to the one that it's been searched for. It uses a formula derived from the equation of a straight line.

$$
mid=Lo+\frac{(Hi - Lo)}{A[Hi]-A[Lo]} * (X-A[Lo])
$$
Where:\
A = array\
Hi = Highest index of the array\
Lo = Lowest index of the array\
X = searched element
