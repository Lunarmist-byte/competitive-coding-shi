strr=input()
l=len(strr)
if l%2==0:
    print("invalid")
else:
    strm=l//2
    lh,rh=list(map(int, strr[:strm])), list(map(int, strr[strm+1:]))
    if sum(lh)==sum(rh):
        print("Valid")
    else:
        print("Invalid")
        