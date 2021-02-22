import math
idata=list(map(int,input().split(",")))
#idata=[6,3,6,20,3,6,-15,3,3]
print(idata)
deg=int(math.sqrt(len(idata)))
tdeg=deg
ll=len(idata)
lsum=0
msum=0
while(deg):
    n=deg*deg
    for i in range(0,ll-n+1):
      lsum=sum(idata[i:i+n])
      if(lsum>msum):
          msum=lsum
    deg-=1
print(msum)
deg=tdeg
while(deg):
    n=deg*deg
    for i in range(0,ll-n+1):
      lsum=sum(idata[i:i+n])
      
      if(lsum==msum):
          slist=idata[i:i+n]
          for j in range(deg):
              for k in range(deg):
                  print(slist[j*deg+k],end="\t")
              print()
    deg-=1

          
    


