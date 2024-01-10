class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        
        while head:
            list.append(head.val)
            head = head.next
        
        left = 0
        right = len(list)-1
        
        while left <= right:
            if list[left] == list[right]:
                left += 1
                right -= 1
            else: 
                return False
        
        return True