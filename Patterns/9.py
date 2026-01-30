n = int(input())
a=ord('a')
for i in range(n):
    print(chr(a+(1%26)*(i+i)))