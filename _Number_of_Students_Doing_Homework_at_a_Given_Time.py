n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
l=int(input())
c=0
for i in range(n):
    if a[i]<=l and b[i]>=l:
        c+=1
print(c)