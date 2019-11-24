# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head_ref = head
        c = 1
        
        while head_ref:
            c += 1 if head_ref.next else 0
            head_ref = head_ref.next

        if c == n:
            head = head.next
            return head

        c = c - n
        
        head_ref = head
        
        for _ in range(c-1):
            head_ref = head_ref.next
        else:
            head_ref.next = head_ref.next.next
            
        return head

sol = Solution()

ln1 = ListNode(1)
ln1.next = ListNode(2)
ln1.next.next = ListNode(3)
# ln1.next.next.next = ListNode(9)

sol.removeNthFromEnd(ln1, 1)
