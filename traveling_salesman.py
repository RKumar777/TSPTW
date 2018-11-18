
# coding: utf-8

# In[4]:


import random
import numpy as np
import math
import time
n=21
NFT0=0.4
lam=0.001
cnt=10000
t=60
cij=np.array([[0,34,16,38,21,8,11,26,14,28,36,12,23,12,29,30,33,13,32,23,24],
[34,0,33,25,22,30,24,31,20,34,26,22,16,34,8,36,30,30,36,13,18],
[16,33,0,25,31,8,13,39,20,12,23,15,30,5,26,14,19,4,16,20,16],
[38,25,25,0,39,30,27,49,30,15,2,27,34,30,18,16,7,26,13,19,15],
[21,22,31,39,0,24,18,10,11,38,39,16,6,29,22,40,39,27,42,20,25],
[8,30,8,30,24,0,6,31,13,20,28,8,23,5,24,22,25,5,24,18,16],
[11,24,13,27,18,6,0,27,7,22,26,2,17,11,19,24,24,9,26,13,13],
[26,31,39,49,10,31,27,0,21,48,49,26,16,36,32,50,49,35,52,30,35],
[14,20,20,30,11,13,7,21,0,27,29,5,10,18,17,29,29,16,31,12,15],
[28,34,12,15,38,20,22,48,27,0,13,23,36,17,26,2,8,15,4,22,16],
[36,26,23,2,39,28,26,49,29,13,0,26,34,28,19,13,5,24,11,19,14],
[12,22,15,27,16,8,2,26,5,23,26,0,15,13,17,25,25,11,27,11,12],
[23,16,30,34,6,23,17,16,10,36,34,15,0,28,17,38,35,26,39,15,21],
[12,34,5,30,29,5,11,36,18,17,28,13,28,0,27,19,24,4,21,21,18],
[29,8,26,18,22,24,19,32,17,26,19,17,17,27,0,28,22,23,28,6,10],
[30,36,14,16,40,22,24,50,29,2,13,25,38,19,28,0,8,17,3,24,18],
[33,30,19,7,39,25,24,49,29,8,5,25,35,24,22,8,0,20,6,20,14],
[13,30,4,26,27,5,9,35,16,15,24,11,26,4,23,17,20,0,19,17,14],
[32,36,16,13,42,24,26,52,31,4,11,27,39,21,28,3,6,19,0,24,18],
[23,13,20,19,20,18,13,30,12,22,19,11,15,21,6,24,20,17,24,0,6],
[24,18,16,15,25,16,13,35,15,16,14,12,21,18,10,18,14,14,18,6,0]])
ei=np.array([0,41,88,132,24,0,0,3,0,112,194,0,69,0,146,105,117,0,130,0,174])
li=np.array([345,183,247,275,137,101,76,155,140,255,308,93,202,106,289,263,264,104,233,122,308])
li0=np.array([345,183,247,275,137,101,76,155,140,255,308,93,202,106,289,263,264,104,233,122,308])          
li0.sort()
Sx=[]
for j in range(n):
    for k in range(n):
        if(li[k]==li0[j] and k not in Sx):
            Sx.append(k)
Sx.remove(0)
A=[]
c=0
A.append(cij[0,Sx[0]])
for q in range(n-2 ):
    A.append(max(A[q],ei[Sx[q]])+cij[Sx[q],Sx[q+1]])
    if(A[q+1]<=li[Sx[q+1]]):
        c=c+1
if(c<19):
    print('initial infeasible solution: {}'.format(Sx))
# swapping elements to see for feasibility
B=list(Sx)


for u in range(n-1):
    for v in range(n-1):
        B[u],B[v]=B[v],B[u]
        M=[]
        M.append(cij[0,B[0]])
        d=0
        for q in range(n-2):
            M.append(max(M[q],ei[B[q]])+cij[B[q],B[q+1]])
            if(M[q+1]<=li[B[q+1]]):
                d=d+1
        if(d<19):
            funct=0
            funct=M[-1]+cij[B[-1],0]+((19-d)*(1+(lam*t))/(NFT0))
            if(funct<cnt):
                cnt=funct
                O=list(B)
                pi0=list(O)
        if(d==19):
            Sl=list(B)
            pi0=list(Sl)
        B=list(Sx)

#initial random solution
#initial random infeasible solutions
print('Initial random feasible solution: {}'.format(pi0))
def calculator(pi):
    N=[]
    N.append(cij[0,pi[0]])
    z=0
    l=len(pi)
    funct=0
    for q in range(l-1):
        N.append(max(N[q],ei[pi[q]])+cij[pi[q],pi[q+1]])
        if(N[q+1]<=li[pi[q+1]]):
            z=z+1
    if(z<19 and l==20):
        funct=N[-1]+cij[pi[-1],0]+((19-z)/(NFT0/(1+(lam*t))))
    if(z==19 and l==20):
        funct=N[-1]+cij[pi[-1],0]
    if(l<20):
        funct=N[-1]
    return(np.array([19-z,funct,z==19]))
print('Checking feasibility of initial random solution by feasibility calculator: {}'.format(calculator(pi0)[-1]==1))
def VNS_1_Opt(pi):
    kmax=2
    k=1
    while(k<=kmax):
        if(k==1):
            pi1=N1(pi)
        if(k==2):
            pi1=N2(pi)
        pr0=calculator(pi)
        pr1=calculator(pi1)
        if((((pr1[-1]==1)and(pr0[-1]==1))            and(pr1[1]<pr0[1]))or((pr1[-1]==1)and(pr0[-1]==0))or((pr1[-1]==0)                                                                 and(pr0[-1]==0)and(pr1[0]<pr0[0]))or((pr0[-1]==0)and(pr1[-1]==1))):
            pi=list(pi1)
        else:
            k=k+1
    return(pi)
def N1(pi):
    for i in range(n-3,1):
        remove=cij[pi[i],pi[i+1]]+c[pi[i-1],pi[i]]-c[pi[i-1],pi[i+1]]
        for j in range(i-1,1):
            add=cij[pi[j-1],pi[i]]+cij[pi[i],pi[j]]-cij[pi[j-1],pi[j]]
            gain=add-remove
            if(gain<0)and(ei[pi[j-1]]+cij[pi[j-1],pi[i]]<=li[pi[i]])            and(ei[pi[i]]+cij[pi[i],pi[j+1]]<=li[pi[j+1]]):
                pi1=list(pi)
                pi1.remove(pi[i])
                pi1.insert(j,pi[i])
                if(calculator(pi1)[1]<calculator(pi)[1]):
                    pi=list(pi1)
    return(pi)
def N2(pi):
    for i in range(1,n-3):
        remove=cij[pi[i-1],pi[i]]+cij[pi[i],pi[i+1]]-cij[pi[i-1],pi[i+1]]
        for j in range(i+1,n-3):
            add=cij[pi[j],pi[i]]+cij[pi[i],pi[j+1]]-cij[pi[j],pi[j+1]]
        gain=add-remove
        if(gain<0)and(ei[pi[i]]+cij[pi[j],pi[i]]<=li[pi[i]])and(ei[pi[i]]+cij[pi[i],pi[j+1]]<=li[pi[j+1]]):
            pi1=list(pi)
            pi1.remove(pi[i])
            pi1.insert(j,pi[i])
            if(calculator(pi1)[1]<calculator(pi)[1]):
                    pi=list(pi1)
    return(pi)
def DestructConstruct(pi,d):
    piR=[]
    piD=[]
    piM=[]
    piX=[]
    piQ=[]
    count=10000
    G=list(pi)
    piR=random.sample(G,d)
    for i in (G):
        if i not in(piR):
            piD.append(i)
    piX=list(piD)
    for x in range(d):
        piM=list(piX)
        for y in range(len(pi)-d):
            piM.insert(y,piR[x])
            if(calculator(piM)[1]<count):
                piQ=list(piM)
                count=calculator(piM)[1]
            piM=list(piX)
            count=10000
        piX=list(piQ)
    if(piX==[]):
        return (piR)
    else:
        return(piX)
kmax=((n-1)/5)
pi=VNS_1_Opt(pi0)
pibest=list(pi)
k=1
while(k<=kmax):
    d=k*5
    pi1=DestructConstruct(pi,d)
    pi2=VNS_1_Opt(pi1)
    pc=calculator(pi)
    pc2=calculator(pi2)
    pcbest=calculator(pibest)
    if((((pc2[-1]==1)and(pc[-1]==1))        and(pc2[1]<pc[1]))or((pc2[-1]==1)                    and(pc[-1]==0))or((pc2[-1]==0)                                and(pc[-1]==0)                                         and(pc2[0]<pc[0]))or((pc[-1]==0)                                                        and(pc2[-1]==1))):
        k=1
        pi=list(pi2)
        pc=calculator(pi)
        if((((pc[-1]==1)and(pcbest[-1]==1))and(pc[1]<pcbest[1]))or           ((pc[-1]==1)and(pcbest[-1]==0))or((pc[-1]==0)and(pcbest[-1]==0)                                and(pc[0]<pcbest[0]))or((pcbest[-1]==0)and(pc[-1]==1))):
            pibest=list(pi)
    else:
        k=k+1
print('The best solution obtained after VIG algorithm:{}'.format(pibest))
print('The value of the function is: {}'.format(calculator(pibest)[1]))
print(time.clock())    

