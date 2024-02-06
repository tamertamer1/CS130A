import sys
sys.setrecursionlimit(10**6)
graphdict={}
rulenumb=int(input())
for inp in range(rulenumb):
    line=input()
    firstinp=line.split(":")
    dep=firstinp[1].strip().split(" ")
    for key in dep:
        if key not in graphdict:
            graphdict[key]=[]
        graphdict[key].append(firstinp[0])
vertex=input()
visitednodes=set()
stck=[]
def dfs(visitednodes,graphdict,vertex):
    if vertex in visitednodes:
        return
    visitednodes.add(vertex)
    if vertex in graphdict:
        for val in graphdict[vertex]:
            if val not in visitednodes:
                dfs(visitednodes,graphdict,val)
    stck.append(vertex)
dfs(visitednodes,graphdict,vertex)
for itm in reversed(stck):
    print(itm)