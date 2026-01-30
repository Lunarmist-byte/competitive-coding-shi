n=int(input())
sum1=0
while(n!=0):
    r=n%10
    sum1+=r
    n=n//10
print(sum1)