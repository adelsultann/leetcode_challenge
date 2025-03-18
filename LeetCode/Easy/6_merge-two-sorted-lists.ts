class ListNodee {
    val: number;
    next: ListNode | null;

    constructor(val: number = 0, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    const dummy = new ListNode(0);
    let op = dummy;

    while (list1 !== null && list2 !== null) {
        if (list1.val <= list2.val) {
            op.next = list1;
            list1 = list1.next;
        } else {
            op.next = list2;
            list2 = list2.next;
        }
        op = op.next;
    }

    op.next = list1 || list2;
    return dummy.next;
}