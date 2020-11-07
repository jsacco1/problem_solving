#!/usr/bin/bash 

# Merge k variable-length arrays
# By: James Sacco
# Created: 11/6/2020
# Python3

"""
Description: Given a list of k variable-length lists, output a flatten list comprised of the sublists, ordered by first element. 
The sublists can be assumed to contain no duplicates, either within or among them.
"""


def mergeLists(c, n):
	# merge sublists by comparison.
    i = 0
    merged = []
	# compare current with next sublist.
    if c[i] < n[i]:
        merged = c + n
        return merged
    else:
        merged = c + n
        return merged
 
def mergeSort(lists):  
  	# merge the sublists in the master list.
    
    res = []  
  
   	# merging the lists, looping over them.
    while len(lists) != 1:  
  
        # clears on every iteration,
        res[:] = [] 
  
        for i in range(0, len(lists), 2):  
            if i == len(lists) - 1: 
                res.append(lists[i])  
  
            else: 
                res.append(mergeLists(lists[i],  
                                            lists[i + 1]))  
  
        lists = res[:]  
    
    return lists

if __name__ == "__main__": 
    test = [[1, 6],  [9, 10, 11],  [24, 35], [14, 15, 16]] 


    sortedlists = mergeSort(test)

    for i in range(0, len(sortedlists)):  
        print(sortedlists[i], end = " ")  
