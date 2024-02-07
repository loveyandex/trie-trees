A=[23,-23,5,1,5,6,2,0,-9,-6]
A=[-23, -9, -6, 0, 1, 2, 5, 5, 6, 23]
kiri_face=0
for i in range(len(A)):
      has_at_least_bubble=False
      for j in range(len(A)-1,i,-1):
            kiri_face+=1
            if A[j]<A[j-1]:
                  has_at_least_bubble=True
                  c=A[j]
                  A[j]=A[j-1]
                  A[j-1]=c
      if has_at_least_bubble is not True:
            break
      
      
      

print(A)
print(kiri_face) 
