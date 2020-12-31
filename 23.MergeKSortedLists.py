# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.merge2Lists(lists[0], lists[1])
        else:
            # return self.approach1(lists)
            return self.approach2(lists)
            
    def approach1(self, lists):
        odd_l = len(lists) % 2 == 1
        x = []
        for i in range(0, len(lists) - 1, 2):
            x.append(self.merge2Lists(lists[i], lists[i+1]))
        if odd_l:
            x.append(lists[-1])
        return self.mergeKLists(x)

    def approach2(self, lists):
        mid_index = len(lists) // 2
        return self.merge2Lists(self.mergeKLists(lists[:mid_index]), self.mergeKLists(lists[mid_index:]))
            
    def merge2Lists(self, l1, l2):
        dummy_node = ListNode()
        it = dummy_node
        
        while l1 and l2:
            if l1.val < l2.val:
                it.next = l1
                l1 = l1.next
            else:
                it.next = l2
                l2 = l2.next
            it = it.next
            
        if l1:
            it.next = l1
        else:
            it.next = l2
            
        return dummy_node.next
        