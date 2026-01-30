q=list(map(int,input().split()))
l,r=0,len(q)-1
while l<r:
    if q[l]%2!=0:
        l+=1
    elif q[r]%2==0:
        r-=1
    else:
        q[l],q[r]=q[r],q[l]
print(q)
#takes an i/p list and sorts odd to left and right even