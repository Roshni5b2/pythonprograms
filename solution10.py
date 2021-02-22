data="ABAABXAABA"
i=0
j=len(data)-1
prev=data[0]
while(True):
    if(i>=j):
        break
    if data[i]!=data[j] or data[j]!=prev:
        break
    i+=1
    j-=1
if i==0:
    print(-1)
else:
    print(i)
    
    
