#!/usr/bin/python3
"""
This module defines a Node class and a SinglyLinkedList class.
"""


class Node:
    """
    Class representing a node in a singly linked list.

    Attributes:
        __data (int):representing the data of the node.
        __next_node (Node):representing the next node in the list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Parameters:
            data (int): Data of the node.
            next_node (Node, optional): Next node in the list.

        Raises:
            TypeError: If data is not an integer.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving the data of the node.

        Returns:
            int: Data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for setting the data of the node.

        Parameters:
            value (int): Data to be set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving the next node in the list.

        Returns:
            Node: Next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the next node in the list.

        Parameters:
            value (Node): Next node to be set.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """
    Class representing a singly linked list.

    Attributes:
        __head:representing the head of the list.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance with an empty list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position.

        Parameters:
            value (int): Value of the new node.
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the entire list.

        Returns:
            str: String representation of the list.
        """
        result = ""
        current = self.__head

        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node

        return result.rstrip("\n")


if __name__ == "__main__":
    SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
