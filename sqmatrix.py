import math
data=input().split(",")
idata=[]
for item in data:
    idata.append(int(item))
#idata=[6,3,6,20,3,6,-15,3,3]
deg=int(math.sqrt(len(idata)))
msum=0
lsum=0
ll=len(idata)
while(deg):
    n=deg*deg
    for i in range(0,ll-n+1):
        lsum=sum(idata[i:i+n])
        if(lsum>msum):
            msum=lsum
    deg-=1
deg=int(math.sqrt(len(idata)))
while(deg):
    n=deg*deg
    for i in range(0,ll-n+1):
        slist=idata[i:i+n]
        lsum=sum(slist)
        if(lsum==msum):
            for j in range(0,deg):
                for k in range(0,deg):
                    print(slist[j*deg+k],end="\t")
                print()
    deg-=1

print("Max Sum:",msum)
    
        
    
