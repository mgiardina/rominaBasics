# Algorithms 

## Bubble Sorting
For each element of the array, a comparison between adjacents elements is made. If the second element of the array is smaller than the first element,  they swap their position. Then the third element is compared with the second and this process continues until the array final element. An the iteration continues until the array is sorted.

<img src="https://cdn.programiz.com/cdn/farfuture/kn1zM7ZGIj60jcTe3mv8gAtbrvFHqxgqfQ7F9MdjPuA/mtime:1582112622/sites/tutorial2program/files/Bubble-sort-0.png" width="200" height="300"/>

## Selection Sorting
It sets the first element of the array as the minimum. This value is compared with the next element of the unsorted array. If the next element is smallest, it is assigned as mininum. This process is applied to the rest items of the array.    

<img src="https://cdn.programiz.com/cdn/farfuture/9jjqXX0fGtJE2ul2Mga20fvf_GkNlFAFsDMwrrwFzbQ/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0-comparision.png" width="200" height="200"/>

## Insertion Sorting
This algorithm splits the array in two, sorted and unsorted. It sets the second element as a key element. If the first element of the array is greater than the key, then key is placed in front of this element which is the sorted part of the array. Then the iteration continues within the unsorted part of the array until the final element is sorted.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/insertionsort.png" width="200" height="200"/>    
  
# Performance
    
  Insertion algorithm has the best performace because it splits the array and works on the unsorted part of it. Bubble algorithm is the worst it terms of performace because all the comparisons are made even if the array is already sorted. This increases the use of computer memory (RAM) as the array elements increase. 

## Example with 1000 element array:  

![performance](performance_sorting.png)


  **Best choise**: Insertion algorithm for its performance in larger arrays.