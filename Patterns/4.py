n=12345
i=0
reversed_n=0
while n>0:
    r=n%10
    arm_n = (arm * 10) + r 
    n=n//10
    i+=1
print(reversed_n)
