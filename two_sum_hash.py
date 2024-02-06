A=[23,2,3,5,1,6,2,4,3,7,6,2,4,8,8,9,14,5,5,15]
S=17
H={}
for i in range(len(A)):
      a=A[i]
      if a in H:
                  print([a,i],H[a])
      else:
            H[S-a]=[a,i]