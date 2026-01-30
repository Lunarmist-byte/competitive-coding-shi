arr = list(map(int, input().split()))
count=0
#duplicate my code
'''duplicates=[]
temp=arr.copy()
for x in arr:
    if x in temp:
        temp.remove(x)
        count+=1
        if x in temp and x not in duplicates:
            duplicates.append(x)
print(duplicates,count)'''
#to print the values
'''for i in arr:
    print(i)
'''
#to duplicate optimized
'''count=0
for i in arr[:]:#creating a copy and do it better by using colon as parameter
    if(arr.count(i)>1):
        count+=1
        for j in range(arr.count(i)):
            arr.remove(i)
        print(arr)
print(count)'''
#show values
ans=[]
print(arr[:])
count=0
for i in arr[:]:
    if(arr.count(i)>1):
        ans.append(i)
       # count+=1
        #for j in range(arr.count(i)):
        #    arr.remove(i)
        #print(arr)
#print(set(ans))#for the duplicate values
print(len(set(ans)))#for just the greatest count
