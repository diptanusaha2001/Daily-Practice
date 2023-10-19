class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True
        fp = sp = head
        while sp: 
            fp, sp = fp.next, sp.next
            if sp: sp = sp.next
        return self.helper(fp, head)[0]
    
    def helper(self, fp: Optional[ListNode], head: Optional[ListNode]) -> tuple[int, ListNode]:
        if not fp.next: 
            return fp.val == head.val, head.next
        is_palindrome, node = self.helper(fp.next, head)
        return is_palindrome and node.val == fp.val, node.next
