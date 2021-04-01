class Solution:
    def insert_list(self, head):
        stack = []
        while(head):
            stack.append(head.val)
            head = head.next
        return stack
    
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        reverse_stack = self.insert_list(head)
        while(head):
            if(head.val == reverse_stack.pop()):
                head = head.next
            else:
                return False
        return True
