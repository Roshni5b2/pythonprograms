strings=input().split(",")
for string in strings:
    words=string.split(":")
    sqsum=0
    for c in words[1]:
        sqsum+=int(c)*int(c)
    if(sqsum%2==0):
        str=words[0][-1]+words[0][:-1]
    else:
        str=words[0][2:]+words[0][:2]
    print(str)    
