class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
#This works using Floyd's algo which uses slow and fast pointers, when the fast pointer reaches at the end, the slow would be at the middle