l=list(map(int,input().split()))
i,j=0,len(l)-1
while(i<j):
    while(l[i]%2!=0 & i<j):
        i+=1
    while(l[i]%2==0 & i<j):
        j-=1
    l[i],l[j]=l[j],l[i]
    i+=1
    j-=1
print(l)
