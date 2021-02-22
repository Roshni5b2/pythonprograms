lst1=['[','{','(']
lst2=[']','}',')']
indata="[[()]"
stk=[]
i=1
for item in indata:
    if item in lst1:
        stk.append(item)
    elif item in lst2:
        if len(stk)==0:
            print(i)
            break
        pitem=stk.pop()
        if lst1.index(pitem)!=lst2.index(item):
            print(i)
            break
    i+=1
else:
    if len(stk)==0:
        print(0)
    else:
        print(i)
            
        
