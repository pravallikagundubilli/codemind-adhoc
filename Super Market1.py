a=int(input())
b=[]
x=[]
q=[]
k=[]
b = [int(i) for i in input().split()][:a]
c=int(input())
d=set(b)
d=list(d)
d.reverse()

for i in d:
    p=b.count(i)
    x.append(p)
    
a=max(x)
for i in range(0,c):
    p=x.index(max(x))
    if a==max(x):
        q.append(d[p])
    else:
        q.sort(reverse=True)
        k.extend(q)
        q=[]
        a=max(x)
        q.append(d[p])
    x[p]=0
q.sort(reverse=True)
k.extend(q)   
for i in k:
    print(i,end=' ')