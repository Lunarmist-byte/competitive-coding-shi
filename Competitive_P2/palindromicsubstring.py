s=input().strip()
n=len(s)
count=0
def expand(l,r):
    global count
    while l>=0 and r<n and s[l]==s[r]:
        count+=1
        l-=1
        r+=1
for i in range(n):
    expand(i,i)
    expand(i,i+1)
print(count)