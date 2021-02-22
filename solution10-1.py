data="AAAABXAAAB"
i=0
ln=len(data)
mid=ln//2
st2=mid
if ln%2==1:
    st2+=1
first=data[:mid]
second=data[st2:]
i=0
nummat=mid
while(i<mid):
    if first[i]!=second[i]:
        nummat-=1
    i+=1
print(mid)
"""if i==0:
    print(-1)
else:
    print(i)"""
    
    
