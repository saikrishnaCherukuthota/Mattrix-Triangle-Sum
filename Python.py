n=int(input())
l=[]
for j in range(n):
    p=list(map(int,input().split(" ")))
    l.append(p)
up_sum=0
lr_sum=0
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            up_sum+=l[i][j]
        if i+j>=n-1:
            lr_sum+=l[i][j]
print(up_sum)
print(lr_sum)
