#Part 1


#Imports
import matplotlib.pyplot as plt
import random
import time
import pandas as pd
#Global Variables Declarations
N=6000000
m=100000
k=69
mainseed=25
p= 2147483647
#seeds generator
seeds=[]
for i in range(k):
    random.seed(time.time_ns())
    seeds.append(int((random.random()*1000000000)))
#Hash Function 1
def hashtemp1(seeed,x,m):
    random.seed(seeed+x)
    return int(random.random()*m)
#Hash Function 2
def hashtemp2 (seeed,x,m):
    random.seed(seeed)
    a=int(random.randint(1,p-1))
    b=int(random.random()*p)
    return ((a*x+b)%p)%m
#Test
x=[]
y=[]
z=[]
while (len(x)<300):
    random.seed(int(time.time_ns()))
    xval=random.randint(0,N-1)
    x.append(xval)
    y.append(hashtemp1(seeds[3],xval,m))
    z.append(hashtemp2(seeds[3],xval,m))
plt.scatter(x,y)
plt.show()


#Part 2

#HashTable definition
HashTable=[0]*m
n=0
#Add(x) function:
def add(x,k,m,hashfun):
  for i in range(k):
    if hashfun==1:
      HashTable[hashtemp1(seeds[i],x,m)]=1
    if hashfun==2:
      HashTable[hashtemp2(seeds[i],x,m)]=1

def contains(x,k,m,hashfun):
  contains=0
  HashValues=0
  for i in range(k):
    if hashfun==1:
      if (HashTable[hashtemp1(seeds[i],x,m)]==1):
        contains +=1
    if hashfun==2:
      if (HashTable[hashtemp2(seeds[i],x,m)]==1):
        contains +=1
  if contains==k:
    return True
  else:
    return False



#Part 3


#Hash 1, c = 10
n=10000
nset=set()
falsepositives=[]
rates=[]
c=10
hashfun=1
test=[]
for i in range(30000):
   a=int(random.randint(1,N-1))
   test.append(a)
for k in range(4,11):
  m=c*n
  falsepositives=[]
  for redo in range(10):
    nset=set()
    numfalse=0
    HashTable=[0]*m
    for ni in range(n):
      nset.add(ni)
      add(ni,k,m,hashfun)
    for ni in test:
      if (contains(ni,k,m,hashfun) and (ni not in nset)):
        numfalse+=1
    falsepositives.append((numfalse/len(test)))
  rates.append(sum(falsepositives)/len(falsepositives))
print(rates)

#Hash 2, c = 10
n=10000
nset=set()
falsepositives=[]
rates=[]
c=10
hashfun=2
test=[]
for i in range(30000):
   a=int(random.randint(1,N-1))
   test.append(a)
for k in range(4,11):
  m=c*n
  falsepositives=[]
  for redo in range(10):
    nset=set()
    numfalse=0
    HashTable=[0]*m
    for ni in range(n):
      nset.add(ni)
      add(ni,k,m,hashfun)
    for ni in test:
      if (contains(ni,k,m,hashfun) and (ni not in nset)):
        numfalse+=1
    falsepositives.append((numfalse/len(test)))
  rates.append(sum(falsepositives)/len(falsepositives))
print(rates)


#Hash 1, c = 15
n=10000
nset=set()
falsepositives=[]
rates=[]
c=15
hashfun=1
test=[]
for i in range(30000):
   a=int(random.randint(1,N-1))
   test.append(a)
for k in range(6,16):
  m=c*n
  falsepositives=[]
  for redo in range(10):
    nset=set()
    numfalse=0
    HashTable=[0]*m
    for ni in range(n):
      nset.add(ni)
      add(ni,k,m,hashfun)
    for ni in test:
      if (contains(ni,k,m,hashfun) and (ni not in nset)):
        numfalse+=1
    falsepositives.append((numfalse/len(test)))
  rates.append(sum(falsepositives)/len(falsepositives))
print(rates)


#Hash 2, c = 15
n=10000
nset=set()
falsepositives=[]
rates=[]
c=15
hashfun=2
test=[]
for i in range(30000):
   a=int(random.randint(1,N-1))
   test.append(a)
for k in range(6,16):
  m=c*n
  falsepositives=[]
  for redo in range(10):
    nset=set()
    numfalse=0
    HashTable=[0]*m
    for ni in range(n):
      nset.add(ni)
      add(ni,k,m,hashfun)
    for ni in test:
      if (contains(ni,k,m,hashfun) and (ni not in nset)):
        numfalse+=1
    falsepositives.append((numfalse/len(test)))
  rates.append(sum(falsepositives)/len(falsepositives))
print(rates)