# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            end = prev

            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next

            curr = prev.next
            next_group = end.next

            prev_node = next_group

            while curr != next_group:
                temp = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = temp

            temp = prev.next
            prev.next = end
            prev = temp 