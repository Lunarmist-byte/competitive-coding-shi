m=int(input())
l=int(input())
for i in range(m):
    for j in range(l):
        if (i==0 or i==m-1 or j==0 or j==l-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

