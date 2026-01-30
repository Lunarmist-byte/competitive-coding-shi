n=int(input("Enter the number"))
mat=[[0]*n for _ in range(n)]
dirs=[(0,1),(1,0),(0,-1),(-1,0)]
r=c=0
d=0

for num in range(1,n*n+1):
    mat[r][c]=num
    nr=r+dirs[d][0]
    nc=c+dirs[d][1]

    if nr<0 or nr>=n or nc<0 or nc>=n or mat[nr][nc]!=0:
        d=(d+1)%4
        nr=r+dirs[d][0]
        nc=c+dirs[d][1]
    r,c=nr,nc
for row in mat:
    print(*(f"{x:3d}" for x in row))
