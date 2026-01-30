n=int(input())
width=(2*n)-1
for i in range(1,n+1):
    num=(int('1'*i)**2)
    print(str(num).center(width))
'''for i in range(1,n+1):
        print('-'*(n-i),end="")
        for j in range(i):
            print(j+1,end="")
        for j in range(i-1,0,-1):
            print(j, end="")
        print()'''