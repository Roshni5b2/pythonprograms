import string as sf
s1="b@1$rd"
print(s1)
data=list(s1)
i=0
j=len(data)-1
while(True):
    if(i>=j):
        break
    if data[i]in sf.punctuation:
        i+=1
        continue
    if data[j]in sf.punctuation:    
        j+=1
        continue
    tc=data[i]
    data[i]=data[j]
    data[j]=tc
    i+=1
    j-=1
print(''.join(data))    
    

