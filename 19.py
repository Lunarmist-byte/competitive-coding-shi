'''n=input()
vowel=0
for i in range(len(n)):
    if(n[i] in {'a','e','i','o','u'}):
        vowel+=1
print(vowel)'''
#palindromw
n=input()
'''i=0
j=len(n)-1
while i<j:
    if n[i]!=n[j]:
        print(False)
        break    
    i+=1
    j-=1
    print(True)''' 
#unique char first seen
freq = {}
for ch in n:
    freq[ch] = freq.get(ch, 0) + 1
found = False
for ch in n:
    if freq[ch] == 1:
        print(ch)
        found = True
if not found:
    print(None)