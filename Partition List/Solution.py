class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_1 = ListNode(0, head)
        dummy_2 = ListNode(0, head)

        p, h = dummy_1, head
        n = dummy_2

        while h:
            if h.val<x:
                n.next = h
                n = n.next
                p.next = h.next
            else:
                p = h
            h = h.next
        n.next = dummy_1.next

        return dummy_2.next
