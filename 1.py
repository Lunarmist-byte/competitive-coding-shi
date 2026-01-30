time=int(input())
n=int(input())
k=time%(2*(n-1))
if k<n:
    print(k+1)
else:
    print(2*n-1-k)
    