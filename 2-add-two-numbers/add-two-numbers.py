class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = 0
        place = 1
        temp = l1
        while temp:
            num1 += temp.val * place
            place *= 10
            temp = temp.next

        num2 = 0
        place = 1
        temp = l2
        while temp:
            num2 += temp.val * place
            place *= 10
            temp = temp.next

        total = num1 + num2

        if total == 0:
            return ListNode(0)

        dummy = ListNode()
        current = dummy

        while total > 0:
            current.next = ListNode(total % 10)
            current = current.next
            total //= 10

        return dummy.next