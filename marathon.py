print("enter number of participants")
N=int(input())
narr=[]
for i in range(0,N):
    narr.append(i)
print("enter time")
time=int(input())
candidatedata=[[]for i in range(N)]
candidatescore=[[]for w in range(N)]
distance=[[]for i in range(N)]
points=[]
for i in range(100):
    points.append(0)

for j in range(N):
    print("enter details of candidate",[j+1])
    for k in range(time+1):
        x=int(input())
        candidatedata[j].append(x)
for i in range(N):
    x=candidatedata[i][-1]
    distance.append(x)
L=len(candidatedata[1])
for i in range(0,N):
    for k in range(L):
        if k%2!=0:
            candidatescore[i].append(candidatedata[i][k-1]*candidatedata[i][L-1]+candidatedata[i][k]*candidatedata[i][L-1])
for i in range(0,len(candidatescore[1])):
    max=0
    for j in range(0,N):
        if candidatescore[j][i]>max:
            max=candidatescore[j][i]
    for k in range(0,N):
        if max==candidatescore[k][i]:
            break
    points[k]=points[k]+1
for i in range(0,N):
    for j in range(0,len(candidatescore[1])):
        if j!=len(candidatescore[1])-1:
           distance[i].append(candidatescore[i][j]+candidatescore[i][j+1])
for i in range(0,len(distance[1])):
    max=0
    for j in range(0,N):
        if distance[j][i]>max:
            max=distance[j][i]
    for k in range(0,N):
        if max==distance[k][i]:
            break
    points[k]=points[k]+1
max1=0
for i in points:
    if i>max1:
        max1=i
for i in range(len(points)):
    if max1==points[i]:
        break
print("the winner is",i+1)




