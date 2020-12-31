# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        it = head
        carry = 0
                
        while (l1 != None) or (l2 != None):
            if l1 == None:
                s = l2.val + carry
                l2 = l2.next
            
            elif l2 == None:
                s = l1.val + carry
                l1 = l1.next
                
            else:
                s = l1.val + l2.val + carry
                l1, l2 = l1.next, l2.next
            
            it.val = s % 10
            carry = s // 10

            if (l1 != None) or (l2 != None):
                it.next = ListNode()
                it = it.next
        
        if carry != 0:
            it.next = ListNode(carry, None)
          
        return head
                
                
            