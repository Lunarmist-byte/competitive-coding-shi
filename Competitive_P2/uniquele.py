from collections import Counter
s=input().strip()
freq=Counter(s)
unique=min(freq,key=freq.get)
print(unique)