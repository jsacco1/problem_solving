def merge(A, first, middle, last):
  L = A[first:midddle]
  R = A[middle:last+1]
  L.append(99999)
  R.append(99999)
  i = j = 0
  
  #copy the small of L and R back into A
  
  for k in range(first, last+1):
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
  
  
