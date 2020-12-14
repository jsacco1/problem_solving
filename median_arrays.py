#!/usr/bin/env python3 
'''
Return the median of 2 sorted arrays.
'''
'''
author: James Sacco
date: 2020-12-11
'''

import sys

def get_median(arr1, arr2):
    '''
    Combine arrays and get median of resultant array.
    '''
    arr1.extend(arr2)
    res = sorted(arr1)
    l = len(res)
    if l % 2 != 0:
        median = (l+1) // 2
        print(res[median])
    elif l % 2 == 0:
        print( 
            (int(res[(l-1)//2 + 1]) + int(res[(l-1)//2]))/2
        )


if __name__ == "__main__":
    # parse input arrays
    if len(sys.argv) >= 3:
        arr1 = sys.argv[1].split(',')
        arr2 = sys.argv[2].split(',')
        print("input arrays: ", arr1, arr2)
        get_median(arr1 = arr1, arr2 = arr2)
    else:
        print("Input required arguments: array1, array2.\nExample: python3 median_arrays.py 1,2 3,4")
    
