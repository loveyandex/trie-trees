

A=[23,-23,5,1,5,6,2,0,-9,-65,-23,5,1,5,6,2,0,-9,-65,-23,5,1,5,6,2,0,-9,-65,-23,5,1,5,6,2,0,-9,-65,-23,5,1,5,6,2,0,-9,-65]

A=[-65, -65, -65, -65, -65, -23, -23, -23, -23, -23, -9, -9, -9, -9, -9, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 
5, 5, 5, 5, 6, 6, 6, 6, 6, 23]

def merge_sort(A: list[int]):
   return   merg_sub_sort(A,0,len(A))
     

def merg_sub_sort(A, p,r):
      if p <r:
            q=int((p+r)/2) 
            return merge(merg_sub_sort(A,p,q),merg_sub_sort(A,q+1,r))
      return A[p:r+1]

def merge(X,Y):
      positive_infinity = float('inf')
      X.append(positive_infinity)
      Y.append(positive_infinity)
      Z=[]
      i,j=0,0
      for k in range(len(X)+len(Y)-2):
            if X[i]<Y[j]:
                  Z.append(X[i])
                  i+=1
            else:
                  Z.append(Y[j])
                  j+=1
      
      return Z
                  

X=merge_sort(A=A)
print(X)
