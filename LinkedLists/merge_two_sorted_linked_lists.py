# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        new_ll = ListNode(0) # fake head
        x_ll = new_ll
        
        while l1 or l2:
            if not l1 or not l2:
                x_ll.next = l1 or l2
                return new_ll.next # due to fake head
            elif l1.val >= l2.val:
                x_ll.next = ListNode(l2.val)
                x_ll = x_ll.next
                l2 = l2.next
            else:
                x_ll.next = ListNode(l1.val)
                x_ll = x_ll.next
                l1 = l1.next
        
        return new_ll.next # due to fake head

sol = Solution()

ln1 = ListNode(1)
ln1.next = ListNode(2)
ln1.next.next = ListNode(4)

ln2 = ListNode(1)
ln2.next = ListNode(3)
ln2.next.next = ListNode(4)

sol.mergeTwoLists(ln1, ln2)
