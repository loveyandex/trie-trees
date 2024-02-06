import math

def heapify( A: list[int]):
      for i in range( math.floor(len(A)/2-1), -1, -1):
            A=make_heapify(A,i)
      return A

def make_heapify(A,kk):
      if 2*kk>=len(A):
            return
      if 2*kk+1>=len(A):
            return
      if A[2*kk]<=A[2*kk+1]:
            j=2*kk+1
      else:
            j=2*kk
      if A[j]>A[kk]:
            c=A[kk]
            A[kk]=A[j]
            A[j]=c
            make_heapify(A,j)
      return A      
            
print(heapify([34,-85,0,2,78,88,76,7,-85,0,2,78,88,76,7]))

       

