"""
Doubly Linked List implementation in Python.

This module provides two classes:
1. Node: Represents a node in the doubly linked list.
2. DoublyLinkedList: Represents the linked list with operations:
   - Insert at beginning, end, or specific index
   - Remove from beginning, end, by value, or by index
   - Traversal and string representation
   - Search
   - Change a value at index
   - Reverse the list

Author: [Ahmed Hisham]
License: MIT
"""

class Node:
    """
    Represents a single node in the doubly linked list.

    Attributes:
        value (any): The value stored in the node.
        next (Node): Reference to the next node in the list.
        prev (Node): Reference to the previous node in the list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Doubly Linked List (DLL) implementation.

    Attributes:
        items (int): The number of nodes in the list.
        head (Node): The first node in the list.
        tail (Node): The last node in the list.
    """
    def __init__(self):
        self.items = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        """Check if the list is empty."""
        return self.items == 0

    def insert_at_end(self, value):
        """
        Insert a value at the end of the list.
        
        Args:
            value (any): Value to insert.
        
        Returns:
            True if inserted successfully.
        """
        new_node = Node(value)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.items += 1
        return True

    def insert_at_beginning(self, value):
        """
        Insert a value at the beginning of the list.
        
        Args:
            value (any): Value to insert.
        
        Returns:
            True if inserted successfully.
        """
        new_node = Node(value)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.items += 1
        return True

    def insert_at_index(self, value, index):
        """
        Insert a value at a specific index.
        
        Args:
            value (any): Value to insert.
            index (int): Position to insert at.
        
        Returns:
            True if inserted successfully.
        
        Raises:
            IndexError: If index is out of bounds.
        """
        if index < 0 or index > self.items:
            raise IndexError("Index out of bounds")

        if self.is_empty() or index == 0:
            return self.insert_at_beginning(value)
        elif index == self.items:
            return self.insert_at_end(value)

        if index <= self.items // 2:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.items - index):
                current_node = current_node.prev

        new_node = Node(value)
        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next.prev = new_node
        current_node.next = new_node

        self.items += 1
        return True

    def remove_start(self):
        """
        Remove a node from the beginning of the list.
        
        Returns:
            The removed value.
        
        Raises:
            Exception: If the list is empty.
        """
        if self.is_empty():
            raise Exception("List is empty")

        removed_node = self.head
        if self.items == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            removed_node.next = None

        self.items -= 1
        return removed_node.value

    def remove_end(self):
        """
        Remove a node from the end of the list.
        
        Returns:
            The removed value.
        
        Raises:
            Exception: If the list is empty.
        """
        if self.is_empty():
            raise Exception("List is empty")

        removed_node = self.tail
        if self.items == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            removed_node.prev = None

        self.items -= 1
        return removed_node.value

    def remove_value(self, value):
        """
        Remove a node by value.
        
        Args:
            value (any): The value to remove.
        
        Returns:
            The removed value if found, -1 otherwise.
        
        Raises:
            Exception: If the list is empty.
        """
        if self.is_empty():
            raise Exception("List is empty")

        if self.head.value == value:
            return self.remove_start()
        if self.tail.value == value:
            return self.remove_end()

        current_node = self.head
        while current_node and current_node != self.tail:
            if current_node.value == value:
                pre = current_node.prev
                nex = current_node.next

                pre.next = nex
                nex.prev = pre
                current_node.next = current_node.prev = None
                self.items -= 1
                return current_node.value
            current_node = current_node.next

        return -1

    def remove_at_index(self, index):
        """
        Remove a node by index.
        
        Args:
            index (int): The index of the node to remove.
        
        Returns:
            The removed value.
        
        Raises:
            IndexError: If index is out of bounds.
        """
        if index < 0 or index >= self.items:
            raise IndexError("Index out of bounds")

        if index == 0:
            return self.remove_start()
        if index == self.items - 1:
            return self.remove_end()

        if index <= self.items // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.items - index - 1):
                current_node = current_node.prev

        pre = current_node.prev
        nex = current_node.next

        pre.next = nex
        nex.prev = pre
        current_node.next = current_node.prev = None
        self.items -= 1
        return current_node.value

    def change_value(self, value, index):
        """
        Change the value at a specific index.
        
        Args:
            value (any): New value.
            index (int): Position to change.
        
        Returns:
            True if changed successfully.
        
        Raises:
            Exception: If the list is empty.
            IndexError: If index is out of bounds.
        """
        if self.is_empty():
            raise Exception("List is empty")
        if index < 0 or index >= self.items:
            raise IndexError("Index out of bounds")

        if index <= self.items // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            index = self.items - (index + 1)
            for _ in range(index):
                current_node = current_node.prev

        current_node.value = value
        return True

    def reverse(self):
        """
        Reverse the entire list in-place.
        
        Returns:
            True if reversed successfully.
        """
        if self.items <= 1:
            return

        current = self.head
        self.head, self.tail = self.tail, self.head

        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev

        return True

    def search(self, value):
        """
        Search for a value in the list.
        
        Args:
            value (any): Value to search for.
        
        Returns:
            The index of the value if found, -1 otherwise.
        
        Raises:
            Exception: If the list is empty.
        """
        if self.is_empty():
            raise Exception("List is empty")

        current_node = self.head
        for index in range(self.items):
            if current_node.value == value:
                return index
            current_node = current_node.next

        return -1

    def get_at_index(self, index):
        """
        Get the value at a specific index.
        
        Args:
            index (int): Position of the value to retrieve.
        
        Returns:
            The value at the index.
        
        Raises:
            IndexError: If index is out of bounds.
        """
        if index < 0 or index >= self.items:
            raise IndexError("Index out of bounds")

        if index <= self.items // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.items - index - 1):
                current_node = current_node.prev

        return current_node.value

    def __str__(self):
        """
        Get a string representation of the list.
        
        Returns:
            str: Values joined by <-> arrows.
        """
        if self.is_empty():
            return "List is empty"

        values = []
        current_node = self.head
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next

        return " <-> ".join(values)
