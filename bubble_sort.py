A=[23,-23,5,1,5,6,2,0,-9,-6]
kiri_face=0
for i in range(len(A)):
      for j in range(len(A)-1,i,-1):
            if A[j]<A[j-1]:
                  c=A[j]
                  A[j]=A[j-1]
                  A[j-1]=c
                  kiri_face+=1
      

print(A)
print(kiri_face) 
