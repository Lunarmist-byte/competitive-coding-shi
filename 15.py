#matrox with 0's
'''rows=3
cols=4
mat=[[0 for _ in range(cols)] for _ in range(rows)]
print(mat)'''
#take more than 1 i/p
'''li=list(map(int,input().split()))
print(li)'''
#TAKE MATRIX I/P
'''row=int(input())
colm=int(input())
ans=[]
for i in range(row):
    temp=[]
    for j in range(colm):
        x=int(input())
        temp.append(x)
    ans.append(temp)
print(ans)'''
#to find no of rows and columns
'''li=[[1,2,3],[1,2,3]]
print(len(li))
print(len(li[0]))'''
#second largest
li=[1,4,5,18,19]
li.remove(max(li))
print(max(li))