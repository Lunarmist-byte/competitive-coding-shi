n=int(input())
cou=1
for i in range(n):
    a=list(range(cou,cou+n)) if i%2==0 else list(range(cou+n-1,cou-1,-1))
    cou+=n
    for j in a:
        print("%5d"%j,end=" ")
    print()