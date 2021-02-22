"""mat1=[[7,8,9,5,4,2],[5,7,9,4,5,2],[6,8,7,9,2,2],
      [1,4,2,7,6,2],[1,1,1,1,1,4]]"""
mat1=[[7,8,9,5,4,2],
      [7,7,8,4,5,2],
      [7,7,2,8,2,2],
      [7,4,7,7,8,2],
      [7,1,1,1,1,4]]

count=0
outlist=[]
rows=5
for i in range (0,len(mat1)):
    item=mat1[i][0]
    for j in range(1,len(mat1[i])):
        if(mat1[i][j]==item):
            count+=1
            if(count>=3):
                outlist.append(item)
        else:
            item=mat1[i][j]
            count=0

print(outlist)
count=0
i=0
lc=len(mat1[0])
for j in range (0,lc-2):
    j1=j
    item=mat1[i][j1]
    
    for k in range(1,lc-j):
        i+=1
        j1+=1
        print(item,count)
        if(mat1[i][j1]==item):
            count+=1
            if(count>=3):
               outlist.append(item)
        else:
            item=mat1[i][j1]
            count=0    
    i=0

count=0
j=0
lr=rows
for i in range (1,lr-2):
    i1=i
    item=mat1[i1][j]
    for k in range(1,lr-i):
        i1+=1
        j+=1
        print(i1,j,mat1[i1][j])
        if(mat1[i1][j]==item):
            count+=1
            print(i1,j,item,count)
            if(count>=3):
               outlist.append(item)
        else:
            item=mat1[i1][j]
            count=0    
    j=0

print(outlist)        
