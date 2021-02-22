import string
s="@aaa"
even="24680"
lst=list(set(string.digits)&set(s))
lst.sort(reverse=True)
for i in range(len(lst)-1,-1,-1):
    if(lst[i] in even):
        ev=lst[i]
        lst.remove(ev)
        lst.append(ev)
        print(''.join(lst))    
        break
else:
    print(-1)

