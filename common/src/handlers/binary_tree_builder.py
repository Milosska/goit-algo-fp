from common.src.classes import Node


def get_tree_node(heap: list[int], index: int) -> Node | None:
    """Рекурсивно будує вузол бінарного дерева з heap списку."""
    if index >= len(heap):
        return None

    left_elem_index = 2 * index + 1
    right_elem_index = 2 * index + 2

    node = Node(key=heap[index])
    node.left = get_tree_node(heap, left_elem_index)
    node.right = get_tree_node(heap, right_elem_index)

    return node


def get_binary_tree(heap: list[int]) -> Node | None:
    """Побудова бінарного дерева з heap списку."""
    binary_tree_root = get_tree_node(heap, 0)
    return binary_tree_root
