arr = list(map(int, input().split()))
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)
print(arr.reverse)
#reverse a array without built in or slicing