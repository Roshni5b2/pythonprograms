#inData=[3,5,8,2,19,12,7,11]
inData=[1,2,7]
inData.sort()
print(inData)
lstLists=[]
lst=[]
maxlen=0
for i in range(0,len(inData)-2):
    for j in range(i+1,len(inData)-1):
        lst=[]
        lst.append(inData[i])
        lst.append(inData[j])
        while(True):
            if(sum(lst[-2:])in inData):
                lst.append(sum(lst[-2:]))
            else:
                break
        if(len(lst)>2):
            if len(lst)>maxlen:
               lstLists=[]
               lstLists.append(lst)
               maxlen=len(lst)
            elif len(lst)==maxlen:
               lstLists.append(lst)
if(len(lstLists)>0):
    print(lstLists[0])
else:
    print(-1)

    
    

