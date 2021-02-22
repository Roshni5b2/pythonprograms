indata="A@bcd1aexz"
uniq=""
start=0
cseq=""
i=0
ln=len(indata)
while(i<ln):
    ch=indata[i]
    if ch.upper() not in cseq.upper():
        cseq+=ch
        i+=1
    else:
        if len(cseq)>len(uniq):
            uniq=cseq
        start+=1
        i=start
        cseq=""
if len(cseq)>len(uniq):
            uniq=cseq 
print(uniq)
        
        
