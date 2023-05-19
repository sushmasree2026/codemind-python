def happy(n):
    r=s=0;
    while(n>0):
        r=n%10
        s=s+(r*r)
        n=n//10
    return s
n=int(input())
temp=n
while (temp!=1 and temp!=4):
    temp=happy(temp)
if temp==1:
    print('True')
else:
    print('False')