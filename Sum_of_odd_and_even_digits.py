n=int(input())
a=list(map(int,input().split()))
s=0
su=0
for i in range(1,n,+2):
    s+=a[i]
for j in range(0,n,+2):
    su+=a[j]
if(s-su==0):
    print("YES")
else:
    print("NO")