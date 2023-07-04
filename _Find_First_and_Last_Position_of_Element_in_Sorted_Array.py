n=int(input())
a=list(map(int,input().split()))
l=int(input())
c=-1
d=-1
for i in range(n):
    if a[i]==l and c==-1:
        c=i
    if a[i]==l:
        d=i
print(c,d)