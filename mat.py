mat1=[[7,8,9,5,4,2],
      [6,7,8,4,5,2],
      [7,6,7,8,2,2],
      [7,7,6,7,8,2],
      [2,3,6,6,8,2]]
count=0
outlist=[]
rows=5

i=0
nc=len(mat1[0])
for j in range (0,nc-3):
    j1=j
    item=mat1[i][j]
    for k in range(1,nc-j-1):
        i+=1
        j1+=1
        if(i>=rows):
            break
        if(mat1[i][j1]==item):
            count+=1
            if(count>=3):
                outlist.append(item)
                count=0
        else:
            item=mat1[i][j1]
            count=0
    i=0

j=0
for i in range (1,rows-3):
    i1=i
    item=mat1[i1][j]
    for k in range(1,rows-i):
        i1+=1
        j+=1
        if(j>=nc):
            break
        if(mat1[i1][j]==item):
            count+=1
            if(count>=3):
                outlist.append(item)
                count=0
        else:
            item=mat1[i1][j]
            count=0
    j=0

print(min(outlist))
