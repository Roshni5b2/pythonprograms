ip=input()
c=0
el=[]
ol=[]
for i in ip:
    if not(i.isnumeric() or i.isalpha()):
        c+=1
    if(i.isnumeric()):
        if(int(i)%2 == 0):
            el.append(i)
        else:
            ol.append(i)
for i in range(min([len(ol),len(el)])):
    if c%2 ==0:
        print(el[i],end='')
        print(ol[i],end='')
    else:
        print(ol[i],end='')
        print(el[i],end='')
if(len(ol)):
    print(''.join(ol[i+1:]))
if(len(el)):
    print(''.join(el[i+1:]))

