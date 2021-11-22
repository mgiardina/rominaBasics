# Searching algorithms 

## Linear searching
Linear search algorithm is the simplest one. Sequentially read each element one by one on a given array until desired element is found. This method may be not effective for arrays with large number of items.

<img src="https://www.tutorialspoint.com/data_structures_algorithms/images/linear_search.gif" width="300" height="100"/>

## Binary searching
Binary search needs a sorted array to start the process. So, if the elements are not sorted, the array must be sorted for the implementation. This algorithm can be implemented with an iterative method or a recursive method.
This method search the middle element of an array and it compares this value with the value being searched. If searched value is in the middle, then this position is return. Else, if the searched value is greater than the middle one, the process is made within the upper half. Otherwise, the lower half is used. This process is made until the searched element is found. 