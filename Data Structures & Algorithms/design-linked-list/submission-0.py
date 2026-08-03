class MyLinkedList:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = self.ListNode()  # dummy head
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head.next

        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = self.ListNode(val, self.head.next)
        self.head.next = new_node

        if self.size == 0:
            self.tail = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = self.ListNode(val)

        self.tail.next = new_node
        self.tail = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index < 0:
            index = 0

        if index == self.size:
            self.addAtTail(val)
            return

        curr = self.head

        for _ in range(index):
            curr = curr.next

        new_node = self.ListNode(val, curr.next)
        curr.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.head

        for _ in range(index):
            prev = prev.next

        node_to_delete = prev.next
        prev.next = node_to_delete.next

        if node_to_delete is self.tail:
            self.tail = prev

        self.size -= 1