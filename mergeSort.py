#!/usr/bin/bash

"""
Description: Mergesort on arr list

# By: James Sacco
# Created: 11/11/2020
# Python3
"""

def mergeSort(arr):
    find_middle(arr, 0, len(arr) - 1)

def find_middle(arr, first, last):
    if first < last:
        mid = (first + last) // 2
        find_middle(arr, first, mid)
        find_middle(arr, mid + 1, last)
        merge(arr, first, mid, last)      
         
def merge(arr, first, mid, last):
    L = arr[first:mid]
    R = arr[mid:last + 1]
    L.append(11111111)
    R.append(11111111)
    i = j = 0
  
    #copy the small of L arrnd R back into arr
    for ele in range(first, last + 1):
        if L[i] <= R[j]:
            arr[ele] = L[i]
            i += 1
        else:
            arr[ele] = R[j]
            j += 1
            
if __name__ == "__main__": 
    arr = [7, 10, 5, 3, 2, 1, 11, 14, 17, 25, 21]

    print(arr)
    mergeSort(arr)
    print(arr)

  
