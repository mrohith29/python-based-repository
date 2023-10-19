# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Compare the values of the two lists' current nodes
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
if __name__ == "__main__":
    list1 = ListNode(1, ListNode(3, ListNode(5)))
    list2 = ListNode(2, ListNode(4, ListNode(6)))

    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)

    print("Merged List:")
    printLinkedList(merged_list)
