graphdict={}
firstinp=input().split()
numppl=firstinp[0]
numconn=firstinp[1]
numdays=firstinp[2]
pplout=0
for i in range(int(numppl)):
    skept=input().split()
    if skept[0] not in graphdict:
        graphdict[skept[0]]=[]
    graphdict[skept[0]].append(int(skept[1]))
    graphdict[skept[0]].append([])
    graphdict[skept[0]].append(0)
for i in range(int(numconn)):
    conn=input().split()
    graphdict[conn[0]][1].append(conn[1])
    if conn[0] not in graphdict[conn[1]][1]:
        graphdict[conn[1]][1].append(conn[0])
rumorstarter=input()
visited=set()
queue=[]
def bfs (rumorstarter):
    global pplout
    queue.append(rumorstarter)
    visited.add(rumorstarter)
    for i in range(int(numdays)):
        qlen=len(queue)
        for k in range(len(queue)):
            pers=queue[0]
            queue.pop(0)
            for con in graphdict[pers][1]:
                if con!=rumorstarter and graphdict[con][2]==0:
                    pplout+=1
                graphdict[con][2]+=1
                if con not in visited and graphdict[con][2]>=graphdict[con][0]:
                    queue.append(con)
                    visited.add(con)
bfs(rumorstarter)
print(pplout)