class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next  # Add this line to update the current pointer

        if list1 is not None:
            current.next = list1
        if list2 is not None:
            current.next = list2

        return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next
    print("None")

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

print("Merged Linked List:")
print_linked_list(merged_head)
