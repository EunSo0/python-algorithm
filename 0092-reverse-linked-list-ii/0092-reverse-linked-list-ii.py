# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = start = ListNode()
        root.next = head
        
        for i in range(left-1):
            start = start.next
        end = start.next
        
        node, prev = start.next, None
        for i in range(right-left+1):
            next = node.next
            node.next = prev
            prev = node
            node = next
            
        start.next = prev
        end.next = node
        
        return root.next