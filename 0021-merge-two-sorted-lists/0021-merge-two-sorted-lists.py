# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Check for empty lists
        if not list1:
            return list2
        if not list2:
            return list1

        # Initialize pointers
        pointer1 = list1
        pointer2 = list2
        merged_head = ListNode() # Head of the merged list
        current = merged_head # Pointer to the current position in the merged list

        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                current.next = pointer1
                pointer1 = pointer1.next
            else:
                current.next = pointer2
                pointer2 = pointer2.next

            current = current.next

        # Handle remaining nodes in either list
        if pointer1 is not None:
            current.next = pointer1
        elif pointer2 is not None:
            current.next = pointer2

        return merged_head.next # Return the head of the merged list