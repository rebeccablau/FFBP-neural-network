"""Implementing the doubly linked list ADT."""


class DLLNode:
    """Doubly Linked list Node."""

    def __init__(self, data):
        """DLL Node constructor."""
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Implementing Doubly Linked List ADT."""

    def __init__(self):
        """Doubly Linked list constructor."""
        self._head = None
        self._tail = None
        self._curr = None

    def add_to_head(self, data):
        """Add a new node to the head of the doubly linked list."""
        new_node = DLLNode(data)
        if self._head:
            self._head.prev = new_node
        new_node.next = self._head
        self._head = new_node
        self.reset_to_head()
        if self._head.next is None:
            self._tail = self._head

    def add_after_current(self, data):
        """Add a new node after the current position."""
        if not self._curr:
            raise IndexError
        new_node = DLLNode(data)
        if self._curr.next is None:
            self._tail = new_node
        else:
            self._curr.next.prev = new_node
        new_node.next = self._curr.next
        self._curr.next = new_node
        new_node.prev = self._curr

    def remove_from_head(self):
        """Remove node from the head of the list and return its data."""
        if not self._head:
            raise IndexError
        return_value = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        else:
            self._head.prev = None
        self.reset_to_head()
        return return_value

    def remove_after_current(self):
        """Remove node after the current node and return its data."""
        if not self._curr or not self._curr.next:
            raise IndexError
        return_value = self._curr.next.data
        self._curr.next = self._curr.next.next
        if self._curr.next is None:
            self._tail = self._curr
        else:
            self._curr.next.prev = self._curr
        return return_value

    def reset_to_head(self):
        """Reset the current pointer to the head."""
        self._curr = self._head

    def reset_to_tail(self):
        """Reset current pointer to tail."""
        self._curr = self._tail

    def move_forward(self):
        """Move forward through the list."""
        if not self._curr or not self._curr.next:
            raise IndexError
        self._curr = self._curr.next

    def move_backward(self):
        """Move backward through the list."""
        if self._curr == self._head:
            raise IndexError
        self._curr = self._curr.prev

    def find(self, data):
        """Find and return an item in the list."""
        temp_curr = self._head
        while temp_curr:
            if temp_curr.data == data:
                return temp_curr.data
            temp_curr = temp_curr.next
        raise IndexError

    def remove(self, data):
        """Find and remove a node."""
        if not self._head:
            raise IndexError
        if self._head.data == data:
            return self.remove_from_head()
        temp_curr = self._head
        while temp_curr.next:
            if temp_curr.next.data == data:
                return_value = temp_curr.next.data
                temp_curr.next = temp_curr.next.next
                if temp_curr.next is None:
                    self._tail = temp_curr
                else:
                    temp_curr.next.prev = temp_curr
                self.reset_to_head()
                return return_value
            temp_curr = temp_curr.next
        raise IndexError

    @property
    def curr_data(self):
        """Return the data at the current position."""
        if not self._curr:
            raise IndexError
        return self._curr.data

    def is_empty(self):
        """Return true if the list is empty, false otherwise."""
        if not self._head:
            return True
        return False
