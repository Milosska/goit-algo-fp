from .Node import Node
from typing import Optional
from task_1.src.algorithms import merge_sort


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            cur = self.head
            while cur.next:
                cur = cur.next

            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return

        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next

        if cur is None:
            return

        if prev is not None:
            prev.next = cur.next

        cur = None

    def search_element(self, data: int) -> Optional[Node]:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur

            cur = cur.next

        return None

    def print_list(self):
        current = self.head
        list_to_show = ""

        while current:
            list_to_show += (
                str(current.data) + " -> " if current.next else str(current.data)
            )
            current = current.next

        print(list_to_show)

    def reverse_list(self) -> None:
        """
        Реверсує зв'язний список виконуючи зміну напрямку посилань між вузлами.
        """
        if self.head is None or self.head.next is None:
            return

        current_node = self.head
        prev_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

    def get_head(self) -> Optional[Node]:
        return self.head

    def sort(self) -> None:
        new_head = merge_sort(self.head)
        self.head = new_head
