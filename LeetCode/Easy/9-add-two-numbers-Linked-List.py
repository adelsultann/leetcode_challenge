# Definition for singly-linked list.
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def addTwoNumbers(self, l1, l2):
        """Adds two numbers represented as linked lists."""
        
        dummy_node = ListNode()  # Dummy node to simplify edge cases
        tail = dummy_node  # Pointer to build the result list
        carry = 0  # Store carry from sum
        
        # Traverse both lists until we reach the end of both
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get value from l1 (0 if l1 is None)
            val2 = l2.val if l2 else 0  # Get value from l2 (0 if l2 is None)
            
            # Compute sum of digits + carry
            total = val1 + val2 + carry
            carry = total // 10  # Compute carry for next iteration | used to extract the first digit for ex val1 = 4 val2 = 6 = 10 | carry = 1
            sum_digit = total % 10  # Get the last digit|if the last digit is 9 then sum_diget will be = 9 

            print(f"Adding: {val1} + {val2} + carry({carry}) = {total} (sum digit: {sum_digit}, new carry: {carry})")
            
            # Append the new digit to the linked list
            tail.next = ListNode(sum_digit)
            tail = tail.next  # Move tail forward
           
            
            # Move l1 and l2 to next node (if exists)
            if l1: 
                l1 = l1.next
            if l2:
                l2 = l2.next
        
       # we return the result list skipping the dummy node which was used to simplify edge cases it was 0
                """tail = dummy_node means tail points to the same object as dummy_node.
        ✅ As we build the linked list, tail moves forward, but dummy_node always stays at the start.
        ✅ The final result starts from dummy_node.next, skipping the dummy placeholder"""
        return dummy_node.next  # Return the result list (skip dummy node)

# Helper function to create a linked list from a Python list
def create_linked_list(values):
    """Converts a list into a linked list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:   
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    """Prints a linked list in a readable format."""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))

# Create linked lists from given Python lists
l1 = create_linked_list([2,4,3])  # Represents 342
l2 = create_linked_list([5,6,4])  # Represents 465

# Print the input lists
print("List 1:")
print_linked_list(l1)

print("List 2:")
print_linked_list(l2)

# Add the two numbers
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Print the result list
print("Sum List:")
print_linked_list(result)
