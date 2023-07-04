n=int(input())
a=list(map(int,input().split()))
ec=int(input())
max=a[0]
for i in range(n):
    if(a[i]>max):
        max=a[i]
for i in range(n):
    c=0
    c=a[i]+ec
    if(c>=max):
        print('True',end=' ')
    else:
        print('False',end=' ')