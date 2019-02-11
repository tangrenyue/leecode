'''
给定两个非空链表，结点元素为非负整数，这些数字从小到大排列。将对应结点的两个数字相加，并返回一个新链表。假设两个链表不以0打头。
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = p = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            l1 = l2 = 0
            if l1:
                carry = l1.val
                l1 = l1.next
            if l2:
                carry = l2.val
                l2 = l2.next
            carry, val = divmod(l1 + l2 + carry, 10)
            p.next = p = ListNode(val)
        return head.next
