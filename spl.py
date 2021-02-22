import string
#data="t9@a42g&516"
data="5u6@n25g7#@"
count=0
lodds=[]
leves=[]
for ch in data:
    if ch in string.punctuation:
        count+=1
    elif ch in string.digits:
        if int(ch)%2==0:
            leves.append(ch)
        else:
            lodds.append(ch)
ol=len(lodds)
el=len(leves)
i=0
if count%2==0:
    while(True):
        if(i<el):
          print(leves[i],end="")
        if(i<ol):
            print(lodds[i],end="")
        i+=1
        if(i>=el and i>=ol):
            break
else:
    while(True):
        if(i<ol):
            print(lodds[i],end="")
        if(i<el):
            print(leves[i],end="")
        i+=1
        if(i>=el and i>=ol):
            break 

