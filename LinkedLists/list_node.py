# https://leetcode.com/problems/add-two-numbers/

import copy # to test with shallow and deep copy

# # Non-recursion (ref class)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result # magic is here (ref binding)
        # result_tail = copy.copy(result) # with shallow copy will not work
        # result_tail = copy.deepcopy(result) # with deep copy will not work as well
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next


sol = Solution()

ln1 = ListNode(2)
ln1.next = ListNode(4)
ln1.next.next = ListNode(3)
ln1.next.next.next = ListNode(9)

ln2 = ListNode(5)
ln2.next = ListNode(6)
ln2.next.next = ListNode(4)
ln2.next.next.next = ListNode(5)

sol.addTwoNumbers(ln1, ln2)



# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# # Recurcion
# class Solution:
#     def addTwoNumbers(self, l1, l2 ,c = 0):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         val = l1.val + l2.val + c
#         c = val // 10
#         ret = ListNode(val % 10 ) 
        
#         if (l1.next != None or l2.next != None or c != 0):
#             if l1.next == None:
#                 l1.next = ListNode(0)
#             if l2.next == None:
#                 l2.next = ListNode(0)
#             ret.next = self.addTwoNumbers(l1.next,l2.next,c)
#         return ret

# sol = Solution()

# ln1 = ListNode(2)
# ln1.next = ListNode(4)
# ln1.next.next = ListNode(3)
# ln1.next.next.next = ListNode(9)

# ln2 = ListNode(5)
# ln2.next = ListNode(6)
# ln2.next.next = ListNode(4)
# ln2.next.next.next = ListNode(5)

# sol.addTwoNumbers(ln1, ln2)

