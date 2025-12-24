from typing import Optional
from task_1.src.classes.Node import Node


def merge_sort(list_head: Optional[Node]) -> Optional[Node]:
    """
    Сортує однозв’язний список за допомогою алгоритму сортування злиттям.
    """
    left_list_head = list_head

    if left_list_head is None or left_list_head.next is None:
        return list_head

    slow = left_list_head
    fast = left_list_head.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    right_list_head: Optional[Node] = slow.next
    slow.next = None

    return merge_nodes(merge_sort(left_list_head), merge_sort(right_list_head))


def merge_nodes(
    left_list_node: Optional[Node], right_list_node: Optional[Node]
) -> Optional[Node]:
    """
    Об’єднує два відсортовані однозв’язні списки в один відсортований список.
    """
    merged_head = None
    current = None

    while left_list_node and right_list_node:
        if left_list_node.data <= right_list_node.data:
            if current is None:
                merged_head = left_list_node
                current = merged_head

            else:
                current.next = left_list_node
                current = current.next

            left_list_node = left_list_node.next

        else:
            if current is None:
                merged_head = right_list_node
                current = merged_head

            else:
                current.next = right_list_node
                current = current.next

            right_list_node = right_list_node.next

    while left_list_node:
        if current is None:
            merged_head = left_list_node
            current = merged_head

        else:
            current.next = left_list_node
            current = current.next
        left_list_node = left_list_node.next

    while right_list_node:
        if current is None:
            merged_head = right_list_node
            current = merged_head

        else:
            current.next = right_list_node
            current = current.next
        right_list_node = right_list_node.next

    return merged_head
