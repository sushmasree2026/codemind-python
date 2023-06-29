n=int(input())
a=list(map(int,input().split()))
x=int(input())
for i in range(x):
    temp=a[0]
    a[0]=a[n-1]
    for j in range(1,n):
        b=a[j]
        a[j]=temp
        temp=b
for i in a:
    print(i,end=" ")