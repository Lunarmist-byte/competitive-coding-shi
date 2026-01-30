n=int(input())
spaces=" "
for i in range(n):
    if i==n-1:
        print("*"*(2*n-1))
    elif i==0:
        print(spaces*(n-1)+"*")
    else:
        outer=spaces*(n-i-1)
        inner=spaces*(2*i-1)
        print(outer + "*" + inner + "*") 