x=int(input("Enter a number:"))
c=0
for i in range(2,x+1):
    if(x%i==0):
        c+=1
if(c==0):
    print("Prime")
else:
    print("Not Prime")
