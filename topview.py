class Node:
    def __init__(self,data):
        self.data=data
        self.hd=0
        self.left = None
        self.right = None
    def insert(self,nd):
        cur=self
        par=self
        
        while(cur):
            par=cur
            if(nd.data<=cur.data):
                cur=cur.left
            else:
                cur=cur.right
        if(nd.data<=par.data):
            par.left=nd
            nd.hd=par.hd-1
        else:
            par.right=nd
            nd.hd=par.hd+1
        print(nd.data,nd.hd)
    def display(self):
        lst=[]
        stk=[self]
        while(len(stk)>0):
            cnd=stk.pop()
            if cnd.hd not in lst:
                print(cnd.data,end="\t")
                lst.append(cnd.hd)
            if cnd.right:
                stk.append(cnd.right)
            if cnd.left:
                stk.append(cnd.left)
data=[10,7,20,15,12,13,40]
root=Node(data[0])
for item in data[1:]:
    cnd=Node(item)
    root.insert(cnd)
root.display()

    
