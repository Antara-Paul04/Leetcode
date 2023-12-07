# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode():
    def __init__(self, val=0, next=None):
        self.val= val
        self.next= next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy= ListNode(0)
        dummy.next=head

        fast=head
        slow=dummy

        while n>0 and fast:
            fast=fast.next
            n-=1
        
        while fast:
            fast=fast.next
            slow=slow.next

        slow.next=slow.next.next
        return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original Linked List:")
print_linked_list(head)

solution = Solution()
new_head = solution.removeNthFromEnd(head, 2)

print("\nLinked List after removing the 2nd node from the end:")
print_linked_list(new_head)

