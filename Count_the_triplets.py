t=int(input())
for i in range(t):
    c=0
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(len(a)):
        for k in range(len(a)):
            if a[j]!=a[k]:
                if a[j]+a[k] in a:
                    c+=1
    if c==0:
        print("-1")
    elif c!=0:
        print(c//2)