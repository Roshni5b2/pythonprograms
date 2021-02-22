class Node:
    count=0
    def __init__(self, data):
        self.id=data
        self.left = None
        self.right = None
        self.color = 0
        self.special=False
        ndstk=[]
    def process(self):
        cnd=self
        ndstk.append(None)
        ndstk.append(cnd)
     
        while(True):
            cnd=ndstk.pop()
            if(not cnd):
                break
          
            if(cnd.color==self.color and not cnd.special):
                cnd.special=True
                Node.count+=1
                
            if(cnd.left):
               ndstk.append(cnd.left)
            if(cnd.right):
               ndstk.append(cnd.right)
        print(self.count)
lNodes=[]
numNodes=int(input())
for i in range(1,numNodes+1):
    nd=Node(i)
    lNodes.append(nd)
for i in range(1,numNodes):
    edge=input().split()
    sid=int(edge[0])
    did=int(edge[1])
    if(not lNodes[sid-1].left):
        lNodes[sid-1].left=lNodes[did-1]
    else:
        lNodes[sid-1].right=lNodes[did-1]
colors=list(map(int,input().split()))
for i in range(0,numNodes):
    lNodes[i].setColor(colors[i])
        
numQueries=int(input())
for i in range(numQueries):
    nid=int(input())
    lNodes[nid-1].process()
