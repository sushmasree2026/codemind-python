n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    s=0
    for j in range(len(a)):
        if a[i]>a[j]:
            s+=1
    l.append(s)
    s=0
for a in l:
    print(a,end=' ')