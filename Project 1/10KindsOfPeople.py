Maplist=[]
visited=[]
Final=[]
mapinput=input().split()
CCMap=[[0 for _ in range(int(mapinput[1]))] for _ in range (int(mapinput[0]))]
for i in range(int(mapinput[0])):
    lineinput=list(input())
    Maplist.append(lineinput)
numqueries=input()
visited=[[False for _ in range (int(mapinput[1]))] for _ in range (int(mapinput[0]))]
def dfs():
    stack=[]
    countnum=0
    for i in range(int(mapinput[0])):
        for k in range(int(mapinput[1])):
            if visited[i][k]==False:
                r1=i
                c1=k
                countnum+=1
                visited[i][k]=True
                CCMap[i][k]=countnum
                stack.append((r1,c1))
                while (len(stack)!=0):
                    r1=stack[-1][0]
                    c1=stack[-1][1]
                    stack.pop()
                    if (r1>0) and (visited[r1-1][c1]==False)and Maplist[r1-1][c1]==Maplist[r1][c1]:
                        visited[r1-1][c1]=True
                        stack.append((r1-1,c1))
                        CCMap[r1-1][c1]=countnum
                    if (r1<int(mapinput[0])-1) and (visited[r1+1][c1]==False)and Maplist[r1+1][c1]==Maplist[r1][c1]:
                        visited[r1+1][c1]=True
                        stack.append((r1+1,c1))
                        CCMap[r1+1][c1]=countnum
                    if (c1>0) and (visited[r1][c1-1]==False) and Maplist[r1][c1-1]==Maplist[r1][c1]:
                        visited[r1][c1-1]=True
                        stack.append((r1,c1-1))
                        CCMap[r1][c1-1]=countnum
                    if (c1<int(mapinput[1])-1) and (visited[r1][c1+1]==False) and Maplist[r1][c1+1]==Maplist[r1][c1]:
                        visited[r1][c1+1]=True
                        stack.append((r1,c1+1))
                        CCMap[r1][c1+1]=countnum
dfs()
for i in range(int(numqueries)):
    inpl=input().split()
    if CCMap[int(inpl[2])-1][int(inpl[3])-1]==CCMap[int(inpl[0])-1][int(inpl[1])-1]:
        if Maplist[int(inpl[0])-1][int(inpl[1])-1]=='1':
            Final.append("decimal")
        else:
            Final.append("binary")
    else:
        Final.append("neither")
for i in range(len(Final)):
    print(Final[i])