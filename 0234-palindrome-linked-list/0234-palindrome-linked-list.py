class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        
        if not head:
            return True
        
        while head:
            list.append(head.val)
            head = head.next

        while len(list) > 1:
            if list.pop(0) != list.pop():
                return False
        
        return True