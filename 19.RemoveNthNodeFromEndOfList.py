# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return head
        
        if head.next == None:
            return None
        
        nodes = [head]
        
        curr_node = head
        
        while curr_node.next != None:
            nodes.append(curr_node.next)
            curr_node = curr_node.next
        
        if n == 1:
            nodes[-2].next = None
            return head
        
        if n == len(nodes):
            return head.next
        
        nodes[-n-1].next = nodes[-n+1]
        return head