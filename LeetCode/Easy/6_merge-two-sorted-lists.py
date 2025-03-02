from typing import Optional

# Define the ListNode class to represent a node in the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # store the value of the node (default is 0)
        self.next = next  # pointer to the next node (default is None)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print("Starting mergeTwoLists function")
        
        dummy_node = ListNode()  # Create a dummy node to simplify edge cases
        tail = dummy_node  # `tail` will help in constructing the merged list
        print(f"Starting merge: tail -> {tail.val} (dummy node)")

        # Merge the two lists while both have elements
        while list1 and list2:
            print(f"Comparing {list1.val} and {list2.val}",f"Comparing list1.next {list1.next} and list2.next{list2.next}")
            if list1.val < list2.val:
                print(f"Attaching list1 node ({list1.val}) to tail")
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                print(f"Attaching list2 node ({list2.val}) to tail")
                list2 = list2.next
            tail = tail.next  # Move tail forward
            print(f"Moved tail to {tail.val}")
        # If any list still has remaining elements, attach them
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
           

        print("Merge complete!")
        print(dummy_node.next)
        return dummy_node.next  # The first node is a dummy, return the next node
    


# Helper function to create a linked list from a Python list
def create_linked_list(values):
    if not values:
        return None  # If the list is empty, return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))


# Create linked lists from given Python lists
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

# Print the input lists
print("List 1:")
print_linked_list(list1)

print("List 2:")
print_linked_list(list2)

# Merge the two lists
solution = Solution()
result = solution.mergeTwoLists(list1, list2)

# Print the merged list
print("Merged List:")
print_linked_list(result)
