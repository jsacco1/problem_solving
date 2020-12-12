#!/usr/bin/env python3 
'''
Return the median of 2 sorted arrays.
'''
'''
author: James Sacco
date: 2020-12-11
'''

import sys

def main(arr1, arr2):
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
            (res[(l-1)//2 + 1] + res[(l-1)//2])/2
        )


if __name__ == "__main__":
    if len(sys.argv) == 3:
        arr1 = [int(i) for i in input().split()]
        arr2 = [int(i) for i in input().split()]
        main(arr1 = arr1,arr2 = arr2)





