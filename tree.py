class Node:
    def __init__(self,nid):
        self.nid=nid
        self.left=None
        self.right=None
        self.color=()
        self.isSpecial=False
lstNodes=[]
numNodes=int(input())
#creating nodes
for i in range(numNodes):
    numNodes[i]=Node(i+1)

#linking the nodes
for i in range(numNodes-1):
    edge=input()
    sid=int(edge[0])
    did=int(edge[1])
    if not lstNodes[sid].left:
        lstNodes[sid].left=lstNodes[did]
    else:
        
    
