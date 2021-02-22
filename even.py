ip=input()
res = ''
me='8'
f=0
for i in ip:
    if (i.isnumeric()):
        res+=i
        if(int(i)%2==0):
            if(i< me):
                me=i
            f=1
if(f and len(res)):
    ss=sorted(res)[::-1]
    ss.remove(me)
    ss=''.join(ss)+me
    print(ss)
else:
    print('-1')


        
