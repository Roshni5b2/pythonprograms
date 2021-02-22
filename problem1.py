class Node:
    count=0
    def __init__(self,nid):
        self.nid=nid
        self.left=None
        self.right=None
        self.color=0
        self.isSpecial=False
    def process(self):
        stk=[]
        cnd=self
        stk.append(None)
        stk.append(cnd)
        while(True):
            cnd=stk.pop()
            if not cnd:
                break
            if cnd.color==self.color and not cnd.isSpecial:
                cnd.isSpecial=True
                Node.count+=1
            if cnd.left:
                stk.append(cnd.left)
            if cnd.right:
                stk.append(cnd.right)
        print("Number of Special Nodes:",Node.count)
    def display(self):
        print(self.nid,end="\t")
        if(self.left):
            print("Left:",self.left.nid,end="\t")
        if(self.right):
            print("Right:",self.right.nid,end="\t")
        print("Color:",self.color)
lstNodes=[]
numNodes=int(input())
#creating the nodes
for i in range(numNodes):
    lstNodes.append(Node(i+1))

#linking the nodes
for i in range(numNodes-1):
    edge=input().split()
    sid=int(edge[0])
    did=int(edge[1])
    if not lstNodes[sid-1].left:
        lstNodes[sid-1].left=lstNodes[did-1]
    else:
        lstNodes[sid-1].right=lstNodes[did-1]

colors=list(map(int,input().split()))
for i in range(numNodes):
    lstNodes[i].color=colors[i]

numQueries=int(input())

for i in range(numQueries):
    nid=int(input())
    lstNodes[nid-1].process()
"""for i in range(numNodes):
    lstNodes[i].display()"""


    
