data=[1,2,3,4,5,6]
n=len(data)
nb=3
cmb=[]
mn=""
mx=""
for i in range(nb-1):
    mn+='1'
    mx+='1'
mn+=str(n-nb+1)
mx=str(n-nb+1)+mx
imn=int(mn)
imx=int(mx)
for i in range(imn,imx+1):
  lst=list(str(i))
  if sum(map(int,lst))==n and '0' not in lst:
      cmb.append(lst)
#print(cmb)
mnsum=0
for lst in cmb:
    start=0
    print(lst,end="")
    lmx=0
    for i in lst:
        ms=sum(data[start:start+int(i)])
        start=start+int(i)
        if ms>lmx:
            lmx=ms
        print(ms,end=" ")
    print()
    if mnsum==0:
        mnsum=lmx
    elif lmx<mnsum:
        mnsum=lmx
print(mnsum)

  

    

