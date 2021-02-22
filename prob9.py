import functools
data=[1,2,3,4,5,6,7,8,9,2]
lft=data.index(5)
rt=data.index(8)
fsum=functools.reduce(lambda a,b:a+b,data[:lft])+\
     functools.reduce(lambda a,b:a+b,data[rt+1:])+\
     int(''.join(list(map(str,data[lft:rt+1]))))
print(fsum)
