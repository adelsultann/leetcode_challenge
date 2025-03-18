// Define the ListNode class
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

// Define the Solution class
class Solution {
    addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
        let dummy = new ListNode(0); // Dummy node to simplify the logic
        let temp = dummy; // Temporary pointer to build the result
        let carry = 0; // Carry-over for addition

        // Iterate through both linked lists
        while (l1 !== null || l2 !== null || carry !== 0) {
            // Get the values of the current nodes (or 0 if the node is null)
            let val1 = l1 ? l1.val : 0;
            let val2 = l2 ? l2.val : 0;

            // Calculate the sum and the new carry
            let sum = val1 + val2 + carry;
            carry = Math.floor(sum / 10); // Update carry
            temp.next = new ListNode(sum % 10); // Create a new node for the result
            temp = temp.next; // Move the temp pointer

            // Move to the next nodes in the input lists
            if (l1 !== null) l1 = l1.next;
            if (l2 !== null) l2 = l2.next;
        }

        // Return the result (skip the dummy node)
        return dummy.next;
    }
}

// Helper function to convert an array to a linked list
function arrayToList(arr: number[]): ListNode | null {
    let dummy = new ListNode(0);
    let temp = dummy;
    for (let num of arr) {
        temp.next = new ListNode(num);
        temp = temp.next;
    }
    return dummy.next;
}

// Helper function to convert a linked list to an array
function listToArray(head: ListNode | null): number[] {
    let result: number[] = [];
    while (head !== null) {
        result.push(head.val);
        head = head.next;
    }
    return result;
}

// Example usage
const l1 = arrayToList([2, 4, 3]); // Convert array to linked list
const l2 = arrayToList([5, 6, 4]); // Convert array to linked list

const solution = new Solution();
const result = solution.addTwoNumbers(l1, l2); // Add the two linked lists

console.log(listToArray(result)); // Convert the result linked list to an array and print