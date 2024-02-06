A=[9,2,4,1,7,76,-7,5,21]
 
####mehtod 1
for i in range(1,len(A),1):
      insing=A[i]
      k=i
      for j in range(i-1,-1,-1):
            if A[j]>insing:
                  A[j+1]=A[j] 
            else: 
                  break      
            k=j
      A[k]=insing           
      print(A)
      
####mehtod 2      
for i in range(1,len(A),1):
      insing=A[i]
      k=0
      for j in range(i-1,-1,-1):
            if A[j]>insing:
                  A[j+1]=A[j] 
            else:
                  A[j+1]=insing
                  break
            if j==0:
                  A[j]=insing
            print("---",A)
      print(A)