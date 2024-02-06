A=[23,-23,5,1,5,6,2,0,-9,-6]




#selection sort what is it ?
# support we can slect each time minimum of remaing list 

for i in range(len(A)):
      min,minj=A[i],i
      for j in range(i+1,len(A)):
            if A[j]<min:
                  min,minj=A[j],j
      
      A[minj]=A[i]
      A[i]=min

print(A)      
            