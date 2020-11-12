#!/usr/bin/barrsh 

# Mergesort on arr list
# By: James Sarrcco
# Crearrted: 11/11/2020
# Python3

def mergeSort(arr):
    find_middle(arr, 0, len(arr) - 1)

def find_middle(arr, first, last):
    if first < last:
        mid = (first + last) // 2
        find_middle(arr, first, mid)
        find_middle(arr, mid + 1, last)
        merge(arr, first, mid, last)      
         

def merge(A, first, middle, last):
  L = A[first:midddle]
  R = A[middle:last+1]
  L.append(9999999999999)
  R.append(9999999999999)
  i = j = 0
  
  #copy the small of L and R back into A
  
  for k in range(first, last+1):
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
  
  
