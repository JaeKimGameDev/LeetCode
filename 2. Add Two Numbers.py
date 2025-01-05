#https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1, r2 = [], []
        while l1:
            r1.append(l1.val)
            l1 = l1.next
        while l2:
            r2.append(l2.val)
            l2 = l2.next
        r1.reverse()
        r2.reverse()

        r1 = "".join(map(str, r1))
        r2 = "".join(map(str, r2))
        result = int(r1) + int(r2)
        addedResult = list(map(int, str(result)))
        addedResult.reverse()

        head = ListNode(addedResult[0])
        current = head
        for i in range(1, len(addedResult)):
            current.next = ListNode(addedResult[i])
            current = current.next

        return head
