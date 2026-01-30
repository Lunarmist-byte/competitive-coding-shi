class Solution:
    def cal(self,piles,mid):
        calh=0
        for i in piles:
            calh+=i//mid
            if(i%mid!=0):
                calh+=1
        return calh
    def minEatingSpeed(self,piles:List[int],h:int)->int:
        start,end=1,max(piles)
        while start<=end:
            mid=(start+end)//2
            calh=self.cal(piles,mid)
            if calh>h:
                start=mid+1
            else:
                end=mid-1
        return start