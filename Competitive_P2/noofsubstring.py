s=input("Enter a string")
b=len(s)
noofsub=(b*(b+1)//2)
print(noofsub)
#NO OF SUBSTRINGS FROM A STRING
for i in range(b):
    for j in range(i,b):
        print(s[i:j+1])
#prinrt substrings of string