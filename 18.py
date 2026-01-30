#find the sum of the diagonals left-right and right-left and difference
arr = list(map(int, input().split()))
n = int(len(arr) ** 0.5)  
d1=0
d2=0
for i in range(n):
    d1+=arr[i*n+1]
    d2+=arr[i*n+(n-1-i)]
print(abs(d1-d2))